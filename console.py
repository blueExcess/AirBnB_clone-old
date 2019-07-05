#!/usr/bin/python3
"""Console for running AirBnB clone."""


import cmd
import sys
import shlex
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
    prompt = '(hbnb) '

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
            args = shlex.split(args)
            a = eval(args[0])()
            a.save()
            print(a.id)

    def do_show(self, args):
        """Prints the class name and id."""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in model_names:
            print("** class doesn't exist **")
            return
        elif len(args) != 2:
            print("** instance id missing **")
            return
        cls, idx = args[0], args[1]
        # try:
        #     eval(args[0])
        # except NameError:
        #     print("** class doesn't exist **")
        #     return

        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        key = cls + '.' + idx

        try:
            obj = obj_dict[key]
            print(obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes the instance indicated and removes it from
        the JSON file."""
        args = shlex.split(args)

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in model_names:
            print("** class doesn't exist **")
            return
        elif len(args) != 2:
            print("** instance id missing **")
            return

        cls, idx = args[0], args[1]
        storage = FileStorage()
        storage.reload()
        obj_dict = storage.all()
        key = cls + '.' + idx

        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()

    def do_all(self, args):
        """Print representation of all instances, or if given
        an argument, all of that class type."""
        obj_list = []
        storage = FileStorage()
        storage.reload()
        objs = storage.all()

        if len(args) != 0:
            if args not in model_names:
                print("** class doesn't exist **")
                return

        for k, v in objs.items():
            if len(args) != 0:
                ka = k.split(".")
                if ka[0] in model_names:
                    obj_list.append(v.__str__())
            else:
                obj_list.append(v.__str__())
        print(obj_list)

    def do_update(self, args):
        """Updates an instance based on the class name and ID
        by either adding or updating given attribute. Also
        saves changes to JSON file."""
        args = shlex.split(args)
        storage = FileStorage()
        storage.reload()

        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in model_names:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        cls, idx, att = args[0], args[1], args[2]
        instance = cls + '.' + idx
        if instance not in obj_dict.keys():
            print("** no instance found **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return

        obj_dict = storage.all()

        try:
            attr_type = type(getattr(object_value, att))
            atty = attr_type(args[3])
        except AttributeError:
            pass

        obj_v = obj_dict[instance]
        setattr(obj_v, att, atty)
        obj_v.save()

    def default(self, args):
        """change default error messages."""
        coms = {'update': self.do_update, 'all': self.do_all,
                'create': self.do_create, 'show': self.do_show,
                'destroy': self.do_destroy}
        args = (args.replace("(", ".").replace(")", ".")
                    .replace('"', "").replace(",", ""))

        try:
            args = args.split(".")
            entry = args[0] + " " + args[2]
            function = coms[args[1]]
            function(entry)
        except:
            print("*** Unknown syntax:", args[0])


model_names = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

if __name__ == '__main__':
    HBNBCommand().cmdloop()
