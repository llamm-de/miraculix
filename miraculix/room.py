"""
Class for room objects.

Author: L. Lamm (lamm@ifam.rwth-aachen.de)
"""
from miraculix.exportable import Exportable
from miraculix.exceptions import *
from miraculix.utils import *
import sqlite3
import os


class Room(Exportable):
    """Class for objects of type Room"""
    def __init__(self, template=None, name=None, internal_id=None, num_seats=None,
                 supervisor_in_charge=None, extra_supervisors=None, assigned_participants=None):
        """Constructor of Room object"""
        if template is not None:
            self.load_template(template)
        else:
            self.Name = name
            self.Internal_ID = internal_id
            self.NumSeats = num_seats
        if not hasattr(self, 'SupervisorInCharge'):
            self.SupervisorInCharge = supervisor_in_charge
        if not hasattr(self, 'ExtraSupervisors'):
            self.ExtraSupervisors = extra_supervisors
        if not hasattr(self, 'AssignedParticipants'):
            self.AssignedParticipants = assigned_participants

    def save_template(self, file='./templates/rooms/room_templates.db'):
        """Save template for room in database"""
        connector = sqlite3.connect(file)
        cursor = connector.cursor()

        "Check if table exists in database"
        if not db_table_exists(cursor, 'rooms'):
            cursor.execute("CREATE TABLE rooms (internal_ID text, name text, num_seats text)")
            connector.commit()

        "Check if room with id already exists"
        cursor.execute("SELECT name FROM rooms WHERE internal_ID = ?", [self.Internal_ID])
        if cursor.fetchone() is not None:
            raise RoomTemplateAlreadyExists("Room template already exists in database!")
        else:
            values = [self.Internal_ID, self.Name, self.NumSeats]
            cursor.execute("INSERT INTO rooms VALUES (?, ?, ?)", values)
            connector.commit()
        connector.close()

    def load_template(self, id_str, file=None):
        """Load template for room from database"""
        if file is None:
            basedir = os.path.dirname(os.path.dirname(__file__))
            file = os.path.join(basedir, r'templates', r'rooms', r'room_templates.db')
        connector = sqlite3.connect(file)
        cursor = connector.cursor()

        if not db_table_exists(cursor, 'rooms'):
            raise TableDoesNotExist("Table does not exist in database")

        cursor.execute("SELECT name FROM rooms WHERE internal_ID = ?", [id_str])
        val = cursor.fetchone()
        if val is None:
            raise RoomTemplateDoesNotExist("Room template does not exists in database!", id_str)
        else:
            self.Internal_ID = id_str
            self.Name = val[0]
            cursor.execute("SELECT num_seats FROM rooms WHERE internal_ID = ?", [id_str])
            self.NumSeats = int(cursor.fetchone()[0])
