#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""

from uuid import uuid4
from datetime import datetime

time_now = datetime.now

class BaseModel:
    """ class BaseModel"""

    def __init__(self, *args, **kwargs):
        """ Public instance attributes initialize """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ update instance attribute with current datetime """
        self.updated_at = datetime.now()


    def to_dict(self):
        """ Returns a dictionary w/ Keys/vals of __dict__ instance
        Return: dictionary w/ all keys/values
        """
        a = dict(self.__dict__)

        for key in a:
            if key == 'id':
                a[key] = self.id
            elif key == 'created_at':
                a[key] = self.created_at.isoformat()
            elif key == 'updated_at':
                a[key] = self.updated_at.isoformat()
            elif key == '__class__':
                a[key] = self.updated_at.isoformat()
            return a
