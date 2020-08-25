"""
Class for protocol objects

Author: L. Lamm (lamm@ifam.rwth-aachen.de)
"""
from miraculix.exceptions import *
from docxtpl import DocxTemplate
import os
import re


class Protocol:
    """Class for objects of type protocol"""
    def __init__(self, exam):
        """Constructor of protocol object"""
        self.Exam = exam

    def make_protocol(self, file, doc_format='docx', lang='german'):
        """Exports protocol"""
        if doc_format == 'docx':
            self.make_docx_protocol(file, lang)
        else:
            raise FormatNotDefined()

    def make_docx_protocol(self, file, lang):
        """Export docx protocol from template"""
        if lang == 'german':
            basedir = os.path.dirname(os.path.dirname(__file__))
            template_file = os.path.join(basedir, r'templates', r'protocols', r'protocol_german_written.docx')
        else:
            raise ProtocolTemplateDoesNotExist()

        for room in self.Exam.Rooms:
            if len(room.AssignedParticipants) > 0:
                doc = DocxTemplate(template_file)

                split_str = re.sub("\.docx$", '', file)
                file_str = split_str + '_' + room.Name + '.docx'

                if room.SupervisorInCharge is None:
                    supervisor = ''
                else:
                    supervisor = room.SupervisorInCharge
                if room.ExtraSupervisors is None:
                    ex_supervisor = ''
                else:
                    ex_supervisor = room.SupervisorInCharge

                participant_list = []
                for participant in room.AssignedParticipants:
                    attributes = [str(participant.Matriculation),
                                  str(participant.Lastname),
                                  str(participant.Firstname),
                                  str(participant.NumberOfTrials)]
                    participant_list.append({'cols': attributes})

                context = {'COURSE': self.Exam.Name,
                           'EXAMINER': self.Exam.Examiner,
                           'DATE': self.Exam.Date,
                           'ROOM': room.Name,
                           'SUPERVISOR': supervisor,
                           'EX_SUPERVISORS': ex_supervisor,
                           'NUM_PARTICIPANTS': len(room.AssignedParticipants),
                           'col_labels': ['Matr.-Nr.', 'Nachname', 'Vorname', 'Versuch'],
                           'tbl_contents': participant_list
                           }
                doc.render(context)
                doc.save(file_str)
                del doc
