"""
Parent class for participant objects.

Author: L. Lamm (lamm@ifam.rwth-aachen.de)
"""
from miraculix.exportable import Exportable
from randomuser import RandomUser
from random import randint


class Participant(Exportable):
    """Class for object of type Participant"""
    def __init__(self, firstname=None, lastname=None, matriculation=None, number_of_trials=None):
        if firstname is not None:
            self.Firstname = firstname
            self.Lastname = lastname
            self.Matriculation = matriculation
            self.NumberOfTrials = number_of_trials
        else:
            self.Firstname = ""
            self.Lastname = ""
            self.Matriculation = 0
            self.NumberOfTrials = 0
        self.Points = []
        self.Grade = 0
        self.Bonus = 0
        self.Annotation = ""

    @staticmethod
    def generate_random_participant():
        """Generates a random participant using randomuser package"""
        user = RandomUser({'nat': 'us'})
        participant = Participant(firstname=user.get_first_name(),
                                  lastname=user.get_last_name(),
                                  number_of_trials=randint(1,3),
                                  matriculation=randint(300000, 500000))
        return participant

    @staticmethod
    def generate_random_participant_list(num_participants):
        lst = []
        for i in range(0, num_participants-1):
            lst.append(Participant.generate_random_participant())
        return lst
