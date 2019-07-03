#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""
from uuid import uuid4
from datetime import datetime
import json
import models


class BaseModel:
    """ class BaseModel"""

    def __init__(self, *args, **kwargs):
        """ Public instance attributes initialize """

        if kwargs:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs['id']
            if key == 'created_at':
                self.created_at = datetime.strptime(kwargs['created_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            if key == 'updated_at':
                self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                if key != '__class__':
                    setattr(self, key, kwargs['__class__'])

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ update instance attribute with current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary w/ Keys/vals of __dict__ instance
        Return: dictionary w/ all keys/values
        """
        dc = self.__dict__.copy()
        dc.update({'__class__': '{}'.format
                   (self.__class__.__name__)})

        for key in dc:
            if key == 'id':
                dc[key] = self.id
            elif key == 'created_at':
                dc[key] = self.created_at.isoformat()
            elif key == 'updated_at':
                dc[key] = self.updated_at.isoformat()

        return dc
