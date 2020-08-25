"""
Class for exam objects

Author: L. Lamm (lamm@ifam.rwth-aachen.de)
"""
from miraculix.utils import read_csv, write_csv, get_index_csv_data
from miraculix.exceptions import *
from miraculix.exportable import Exportable
from miraculix.room import Room
from miraculix.participant import Participant
import re


class Exam(Exportable):
    """Class for objects of type Exam"""
    def __init__(self, input_file=None, name=None, date=None, examiner=None, rooms=None,
                 points_per_task=None, participants=None):
        """Constructor of Exam object"""
        if input_file is not None:
            self.import_data_RWTHOnline(input_file)
        else:
            self.Name = name
            self.Date = date
            self.Examiner = examiner
            self.Participants = participants
            self.Rooms = rooms
        self.Exam_data_file = input_file
        self.Points_per_task = points_per_task

    def save_exam(self, file):
        """Save current exam to .json file"""
        data = self.data2dict()
        self.write_json(file, data)

    def load_exam(self, file):
        """Load exam from .json file"""
        data = self.read_json(file)

        self.Name = data['Name']
        self.Date = data['Date']
        self.Examiner = data['Examiner']
        self.Points_per_task = data['Points_per_task']
        self.Rooms = []
        self.Participants = []
        self.Exam_data_file = data['Exam_data_file']

        for item in data['Rooms']:
            self.Rooms.append(Room(template=item['Internal_ID']))

        for item in data['Participants']:
            self.Participants.append(Participant(item['Firstname'],
                                                 item['Lastname'],
                                                 item['Matriculation'],
                                                 item['NumberOfTrials']))

    def import_data_RWTHOnline(self, file):
        """Imports participant data from .csv file generated in RWTHOnline"""
        self.Participants = []
        data = read_csv(file)
        self.Exam_data_file = file

        "Get indices of data fields in data"
        indices = get_index_csv_data(data, {'lastname': "FAMILY_NAME_OF_STUDENT",
                                            'firstname': "FIRST_NAME_OF_STUDENT",
                                            'matriculation': "REGISTRATION_NUMBER",
                                            'trials': 'GUEL_U_AKTUELLE_ANTRITTE_SPO',
                                            'date': 'DATE_OF_ASSESSMENT',
                                            'title': 'COURSE_TITLE',
                                            'examiner': 'Examiner',
                                            'rooms': 'TERMIN_ORT'})

        "Assign Name, date and examiner to exam"
        self.Name = data[1][indices['title']]
        self.Date = data[1][indices['date']]
        examiner_str = data[1][indices['examiner']]
        if re.findall("Dr\.-Ing\.", examiner_str):
            examiner_str = re.sub("Dr\.-Ing\.", '', examiner_str)
            examiner_str = "Dr.-Ing. " + examiner_str
        if re.findall("Prof\.", examiner_str):
            examiner_str = re.sub("Prof\.", '', examiner_str)
            examiner_str = "Prof. " + examiner_str
        if re.findall("Univ.-", examiner_str):
            examiner_str = re.sub("Univ.-", '', examiner_str)
        self.Examiner = examiner_str

        "Create participants for exam"
        iterator = iter(data)
        next(iterator)
        for item in iterator:
            self.Participants.append(Participant(item[indices['firstname']],
                                                 item[indices['lastname']],
                                                 item[indices['matriculation']],
                                                 item[indices['trials']]))

        " Create rooms for exam"
        self.Rooms = []
        room_str = data[1][indices['rooms']]
        room_str = re.split(", <br>", room_str)
        for index in range(len(room_str)):
            room_id = re.findall("([0-9]{4}\|[0-9]{3})", room_str[index])[0]
            room = Room()
            room.load_template(room_id)
            self.Rooms.append(room)
        self.Rooms.sort(key=lambda x: x.NumSeats, reverse=True)

    def export_data_RWTHOnline(self, file=None):
        """Export data to .csv file for upload to RWTHOnline
            todo: Check if rating has been performed properly
        """
        if file is None:
            file_data = read_csv(self.Exam_data_file)
        else:
            file_data = read_csv(file)

        "Get indices of data fields"
        indices = get_index_csv_data(file_data,
                                     {'matriculation': "REGISTRATION_NUMBER",
                                      'grade': "GRADE",
                                      'annotation': "FILE_REMARK"})

        "Assign grades and annotations"
        iterator = iter(file_data)
        next(iterator)
        for item in iterator:
            matriculation = item[indices['matriculation']]
            for p in self.Participants:
                if p.Matriculation == matriculation:
                    participant = p
                    break
                else:
                    participant = None
            if participant is not None:
                item[indices['grade']] = participant.Grade
                item[indices['annotation']] = participant.Annotation
            else:
                raise DataExportMismatch('Participant with matriculation ' +
                                         matriculation + ' does not exist in list'
                                                         'from RWTHOnline!')

        write_csv(self.Exam_data_file, file_data)

    def export_rating_list(self, file):
        """Export a simple .csv file for rating of the examination"""
        if not self.is_object_initialized():
            raise UninitializedObject('Not able to export rating list. '
                                      'Please first initialize the exam object properly.', self)

        data = []
        header = ['Matriculation', 'Lastname', 'Firstname', 'Trial']
        for i in range(len(self.Points_per_task)):
            header.append('Pts. task ' + str(i+1))
        header.append('Pts. total')
        header.append('Bonus')
        header.append('Grade')
        header.append('Annotation')
        data.append(header)

        row = []
        for part in self.Participants:
            row = [part.Matriculation,
                   part.Lastname,
                   part.Firstname,
                   part.NumberOfTrials]
            for i in range(len(self.Points_per_task) + 4):
                row.append('')
            data.append(row)

        write_csv(file, data)

    def import_rating_list(self, file):
        """Import .csv rating list after rating of exam has been performed"""
        if not self.is_object_initialized():
            raise UninitializedObject('Not able to import rating list. '
                                      'Please first initialize the exam object properly.', self)

        data = read_csv(file)
        iterator = iter(data)
        next(iterator)
        for item in iterator:
            matriculation = item[0]
            for part in self.Participants:
                if part.Matriculation == matriculation:
                    pts = []
                    for i in range(len(self.Points_per_task)):
                        val = item[i+4]
                        if val == '':
                            int_pts = 0
                        else:
                            int_pts = int(val)
                        pts.append(int_pts)
                    part.Points = pts
                    part.Bonus = item[5 + len(self.Points_per_task)]
                    part.Grade = item[6 + len(self.Points_per_task)]
                    part.Annotation = item[7 + len(self.Points_per_task)]

    def assign_participants(self, form='matriculation', rev=False, offset=5):
        """ Assign participants to rooms"""
        if not self.is_object_initialized():
            raise UninitializedObject('Not able to assign participants. '
                                      'Please first initialize the exam object properly.', self)
        self.check_room_capacity(offset)

        if form == 'matriculation':
            self.Participants.sort(key=lambda x: x.Matriculation, reverse=rev)
        elif form == 'lastname':
            self.Participants.sort(key=lambda x: x.Lastname, reverse=rev)

        counter = 0
        for room in self.Rooms:
            room.AssignedParticipants = []
            seats_available = int(room.NumSeats) - (1 + offset)
            seat_count = 0
            while seat_count <= seats_available:
                if counter <= (len(self.Participants) - 1):
                    room.AssignedParticipants.append(self.Participants[counter])
                    seat_count = seat_count + 1
                    counter = counter + 1
                else:
                    break

    def check_room_capacity(self, offset):
        """Check if total room capacity is sufficient"""
        num_part = len(self.Participants)
        num_seats = 0
        for room in self.Rooms:
            num_seats = num_seats + int(room.NumSeats) - offset

        if not (num_seats - num_part) >= 0:
            raise InsuffientCapacity('Number of participants exceeds number of '
                                     'available seats! Please check your room booking process.')