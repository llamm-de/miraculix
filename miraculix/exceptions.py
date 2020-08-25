"""
Package providing exceptions for the MIRACULIX software.

Author: L. Lamm (lamm@ifam.rwth-aachen.de)
"""


class MiraculixError(Exception):
    """Base class for exception in this module"""
    pass


class UninitializedObject(MiraculixError):
    """Exception raised, if object in not initialized properly."""
    def __init__(self, message=None, obj=None):
        if message is None:
            message = 'Object has not been fully initialized! Please check objects attributes.'
        super(UninitializedObject, self).__init__(message)
        self.obj = obj


class DataExportMismatch(MiraculixError):
    """Exception for participant mismatch in export routine"""
    def __init__(self, message):
        super(DataExportMismatch, self).__init__(message)


class InsuffientCapacity(MiraculixError):
    """Exception if total room capacity is less then total number of participants"""
    def __init__(self, message):
        super(InsuffientCapacity, self).__init__(message)


class RoomTemplateAlreadyExists(MiraculixError):
    """Exception if template already exists in database"""
    def __init__(self, message):
        super(RoomTemplateAlreadyExists, self).__init__(message)


class RoomTemplateDoesNotExist(MiraculixError):
    """Exception if template does not exist in database"""
    def __init__(self, message, template_id):
        super(RoomTemplateDoesNotExist, self).__init__(message)
        self.id = template_id
        print(self.id)


class ProtocolTemplateDoesNotExist(MiraculixError):
    """Exception if template does not exist in database"""
    def __init__(self):
        super(ProtocolTemplateDoesNotExist, self).__init__("Protocol template does not exist.")

        
class TableDoesNotExist(MiraculixError):
    """Exception if table does not exist in database"""
    def __init__(self, message):
        super(TableDoesNotExist, self).__init__(message)


class FormatNotDefined(MiraculixError):
    """Exception if format does not exist"""
    def __init__(self):
        super(FormatNotDefined, self).__init__("Format not defined!")
        

class EvaluationModeDoesNotExist(MiraculixError):
    """Exception if evaluation mode does not exist"""
    def __init__(self):
        super(EvaluationModeDoesNotExist, self).__init__("Evaluation mode does not exist.")


class PointsOutOfScope(MiraculixError):
    """Exception if points are out of scope"""
    def __init__(self):
        super(PointsOutOfScope, self).__init__("Points are out of scope.")
