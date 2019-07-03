#!/usr/bin/python3
"""Console for running AirBnB clone."""


import cmd, sys, shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage



class HBNBCommand(cmd.Cmd):
    """Class to create console for project."""
    prompt = '(hbtn) '

    def do_quit(self, args):
        """Quit the console and return to shell.
        Does include a newline before quitting."""
        return True

    def do_EOF(self, args):
        """Will exit command line when reaches EOF.
        Does not print a newline."""
        return True

    def emptyline(self):
        """do nothing on empty line."""
        pass

    def do_create(self, args):
        """Create a new object of specified class, save to JSON
        and print out the id of new object."""
        if len(args) == 0:
            print("** class name missing **")
        elif args not in model_names:
            print("** class doesn't exist **")
        else:
            a = args()
            a.save()
            print(a.id)

    def do_show(self, args):
        """Prints the class name and id."""
        args = shlex.split(args)
        cls, idx  = args[0], args[1]
        if len(args) == 0:
            print("** class name missing **")
            return
        elif cls not in model_names:
            print("** class doesn't exist **")
            return
        elif len(args) != 2:
            print("** instance id missing **")
            return

        storage = FileStorage()
        storage.reload()
        obj_list = storage.all()
        key = cls + '.' + idx

        try:
            obj = obj_list[key]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes the instance indicated and removes it from
        the JSON file."""
        args = shlex.split(args)
        cls, idx = args[0], args[1]
        if len(args) == 0:
            print("** class name missing **")
            return
        elif cls not in model_names:
            print("** class doesn't exist **")
            return
        elif len(args) != 2:
            print("** instance id missing **")
            return

        storage = FileStorage()
        storage.reload()
        obj_list = storage.all()
        key = cls + '.' + idx

        if key in obj_list:
            del obj_list[key]
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Print representation of all instances, or if given
        an argument, all of that class type."""
        pass

    def do_update(self, args):
        """Updates an instance based on the class name and ID
        by either adding or updating given attribute. Also
        saves changes to JSON file."""
        pass


model_names = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

if __name__ == '__main__':
    HBNBCommand().cmdloop()
