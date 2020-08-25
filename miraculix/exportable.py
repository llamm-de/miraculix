"""
Parent class for exportable objects.

Author: L. Lamm (lamm@ifam.rwth-aachen.de)
"""
import json


class Exportable(object):
    """Parent class for .json exportable objects"""
    def __init__(self):
        """Empty constructor"""
        pass

    def data2dict(self, export_list=[]):
        """Store attributes in dictionary for .json export"""
        data = {}
        for attr_name in self.get_attributes():
            attribute = getattr(self, attr_name)
            if not export_list or (attr_name in export_list):
                if isinstance(attribute, list):
                    if attribute and isinstance(attribute[0], Exportable):
                        item_list = []
                        for item in attribute:
                            item_data = item.data2dict()
                            item_list.append(item_data)
                        data[attr_name] = item_list
                    else:
                        data[attr_name] = attribute
                else:
                    data[attr_name] = attribute
        return data

    def print_object_info(self):
        """Print information on object (including its attributes) to console"""
        print('Object of type: ' + str(type(self)))
        print('\tAttributes:')
        attr = self.get_attributes()
        for a in attr:
            print('\t\t' + a)

    def get_attributes(self):
        """Getter for attribute names"""
        attributes = []
        for a in dir(self):
            if not a.startswith('__') and not callable(getattr(self, a)):
                attributes.append(a)
        return attributes

    def is_object_initialized(self):
        """Checks for non initialized attributes"""
        attr = self.get_attributes()
        for a in attr:
            if getattr(self, a) is None:
                return False
        return True

    @staticmethod
    def read_json(file):
        """Read object data from .json file"""
        with open(file) as infile:
            data = json.load(infile)
        return data

    @staticmethod
    def write_json(file, data):
        """Write object data to .json file"""
        with open(file, 'w+') as outfile:
            json.dump(data, outfile, indent=4)