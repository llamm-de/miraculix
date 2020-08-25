"""
Script to generate random user data in RWTHOnline .csv format

Author: L. Lamm (lamm@ifam.rwth-aachen.de)
"""
from miraculix.participant import Participant
from miraculix.utils import write_csv

"""Generate list of participants"""
participant_list = Participant.generate_random_participant_list(50)

"""Arrange Data for .csv export"""
file_data = [['STUDY_PROGRAMME',
              'CODE_OF_STUDY_PROGRAMME',
              'Studienplan_Version',
              'SPO_KKONTEXT',
              'REGISTRATION_NUMBER',
              'FAMILY_NAME_OF_STUDENT',
              'FIRST_NAME_OF_STUDENT',
              'GESCHLECHT',
              'DATE_OF_ASSESSMENT',
              'GUEL_U_AKTUELLE_ANTRITTE_SPO',
              'GRADE',
              'REMARK',
              'Number_Of_The_Course',
              'SEMESTER_OF_The_COURSE',
              'COURSE_TITLE',
              'Examiner',
              'Start_Time',
              'TERMIN_ORT',
              'DB_Primary_Key_Of_Exam',
              'DB_Primary_Key_Of_Candidate',
              'COURSE_GROUP_NAME',
              'FILE_REMARK',
              'EMAIL_ADDRESS',
              'ECTS_GRADE',
              'Information']]

for participant in participant_list:
    file_data.append(['Masterstudium - Musterstudiengang',
                      '9999 99 999',
                      '3000',
                      '[3000] Musteringenieurwesen',
                      str(participant.Matriculation),
                      str(participant.Lastname),
                      str(participant.Firstname),
                      'D',
                      '01.01.3000',
                      str(participant.NumberOfTrials),
                      '',
                      '',
                      '99PV99999',
                      '00W',
                      'Musterwissenschaften',
                      'Max Mustermann Dr.-Ing. Univ.-Prof.',
                      '12:00',
                      'BS I (2131|101), <br>BS II (2131|102)',
                      '999999',
                      '999999',
                      '',
                      '',
                      str(participant.Lastname) + '(at)rwth-aachen.de',
                      ''])

"""Export data to .csv file"""
write_csv('./data/example_inputdata.csv', file_data)
