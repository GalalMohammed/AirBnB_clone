#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter for AirBnB clone"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program
        """
        print()
        return True

    def emptyline(self):
        """do nothing when an empty line + ENTER is pressed
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
