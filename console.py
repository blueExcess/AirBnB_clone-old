#!/usr/bin/python3
"""Console for running AirBnB clone."""


import cmd, sys



class HBNBCommand(cmd.Cmd):
    """Class to create console for project."""
    prompt = '(hbtn) '

    def do_quit(self, args):
        """Quit the console and return to shell."""
        return True

    def do_EOF(self, args):
        """Will exit command line when reaches EOF."""
        return True

    def emptyline(self):
        """do nothing on empty line."""
        pass

    def do_create(self, args):
        """Create a new object of specified class, save to JSON
        and print out the id of new object."""
        pass

    def do_show(self, args):
        """Prints the class name and id."""
        pass

    def do_destroy(self, args):
        """Deletes the instance indicated and removes it from
        the JSON file."""

    def do_all(self, args):
        """Print representation of all instances, or if given
        an argument, all of that class type."""
        pass

    def do_update(self, args):
        """Updates an instance based on the class name and ID
        by either adding or updating given attribute. Also
        saves changes to JSON file."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
