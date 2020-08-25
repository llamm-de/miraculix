"""
Class for evaluator objects

Author: L. Lamm (lamm@ifam.rwth-aachen.de)
"""
import math
from miraculix.exceptions import *


class Evaluator:
    """Class for objects of type evaluator"""
    def __init__(self, exam):
        """Constructor of evaluator object"""
        self.Exam = exam

    def evaluate(self, lower_bound_pct=0.5, upper_bound_pct=0.9, mode='nearest'):
        """Evaluate examination"""
        pt_limits = self.set_pt_limits(lower_bound_pct, upper_bound_pct, mode)

        for participant in self.Exam.Participants:
            if not self.is_grade_note(participant.Grade):
                pts_total_part = sum(participant.Points)
                bonus = participant.Bonus
                grade = self.get_grade(pts_total_part, bonus, pt_limits)
                participant.Grade = grade

    def set_pt_limits(self, lower_bound_pct, upper_bound_pct, mode):
        """Set point limits for grades"""
        pts_total = sum(self.Exam.Points_per_task)
        lower_bound_pts = math.floor(pts_total * lower_bound_pct)
        upper_bound_pts = math.floor(pts_total * upper_bound_pct)
        del_pts = (upper_bound_pts - lower_bound_pts) / 9

        pts_array = [lower_bound_pts]
        for i in range(1, 9):
            pts_array.append(pts_array[i - 1] + del_pts)
        pts_array.append(upper_bound_pts)

        pts_array = self.round_array(pts_array, mode)
        return pts_array

    @staticmethod
    def round_array(array, mode):
        """Round all entries of array according to mode"""
        for i in range(0, len(array)):
            if mode == 'floor':
                array[i] = math.floor(array[i])
            elif mode == 'nearest':
                array[i] = round(array[i])
            elif mode == 'ceil':
                array[i] = math.ceil(array[i])
            else:
                raise EvaluationModeDoesNotExist()
        return array

    @staticmethod
    def get_grade(pts, bonus, pts_array):
        """Calculate grade from points"""
        if pts < pts_array[0]:
            return 5.0
        if not bonus:
            if pts_array[0] <= pts < pts_array[1]:
                return 4.0
            elif pts_array[1] <= pts < pts_array[2]:
                return 3.7
            elif pts_array[2] <= pts < pts_array[3]:
                return 3.3
            elif pts_array[3] <= pts < pts_array[4]:
                return 3.0
            elif pts_array[4] <= pts < pts_array[5]:
                return 2.7
            elif pts_array[5] <= pts < pts_array[6]:
                return 2.3
            elif pts_array[6] <= pts < pts_array[7]:
                return 2.0
            elif pts_array[7] <= pts < pts_array[8]:
                return 1.7
            elif pts_array[8] <= pts < pts_array[9]:
                return 1.3
            elif pts_array[9] <= pts:
                return 1.0
            else:
                raise PointsOutOfScope()
        else:
            if pts_array[0] <= pts < pts_array[1]:
                return 3.7
            elif pts_array[1] <= pts < pts_array[2]:
                return 3.3
            elif pts_array[2] <= pts < pts_array[3]:
                return 3.0
            elif pts_array[3] <= pts < pts_array[4]:
                return 2.7
            elif pts_array[4] <= pts < pts_array[5]:
                return 2.3
            elif pts_array[5] <= pts < pts_array[6]:
                return 2.0
            elif pts_array[6] <= pts < pts_array[7]:
                return 1.7
            elif pts_array[7] <= pts < pts_array[8]:
                return 1.3
            elif pts_array[8] <= pts:
                return 1.0
            else:
                raise PointsOutOfScope()

    @staticmethod
    def is_grade_note(grade):
        """Check for special grade notes of RWTHOnline"""
        """
            B - Bestanden (Passed the exam)
            X - Nicht erschienen (Did not attend)
            NZ - Nicht zugelassen (Inadmissible for examination)
            PA - Prüfung abgebrochen (Cancelled examination)
            U - Ungültig/Täuschung (Invalid / Attempt to deceive)
        """
        if grade == 'B' or grade == 'X' or grade == 'NZ' or grade == 'PA' or grade == 'U':
            return True
        else:
            return False
