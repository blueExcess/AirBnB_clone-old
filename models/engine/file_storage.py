#!/usr/bin/python3
"""
Class FileStorage serializes
 instances to a JSON file and
deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path


class FileStorage:
    """
    class FileStorage to serialize
    instances to Json and deserialize JSON
    file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionay objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        id_of_bm = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[id_of_bm] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        my_dict = {}
        for key in FileStorage.__objects:
            my_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'wt') as myFile:
            json.dump(my_dict, myFile)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'rt') as myFile:
                my_dict = json.load(myFile)
            for key, value in my_dict.items():
                my_dict[key] = eval(value['__class__'])(**value)
