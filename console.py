#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """command interpreter for AirBnB clone"""
    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel,
               'User': User,
               'Place': Place,
               'State': State,
               'City': City,
               'Amenity': Amenity,
               'Review': Review}

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

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.classes[line]()
            print(obj.id)
            storage.save()

    def do_show(self, line):
        """Prints the string representation of an instance
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif not args[0] in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif not args[0] + '.' + args[1] in storage.all().keys():
            print("** no instance found **")
        else:
            print(storage.all()[args[0] + '.' + args[1]])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif not args[0] in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif not args[0] + '.' + args[1] in storage.all().keys():
            print("** no instance found **")
        else:
            del storage.all()[args[0] + '.' + args[1]]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        """
        line = line.strip()
        if line and line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objs_str_list = []
            for v in storage.all().values():
                if line and isinstance(v, HBNBCommand.classes[line]):
                    objs_str_list.append(str(v))
                elif not line:
                    objs_str_list.append(str(v))
            print(objs_str_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif not args[0] in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif not args[0] + '.' + args[1] in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            try:
                args[3] = int(args[3])
            except Exception:
                try:
                    args[3] = float(args[3])
                except Exception:
                    args[3] = args[3][1:-1]
            setattr(storage.all()[args[0] + '.' + args[1]], args[2], args[3])
            storage.save()

    def do_count(self, line):
        """retrieve the number of instances of a class
        """
        arg = line.strip()
        count = 0
        for v in storage.all().values():
            if arg == v.__class__.__name__:
                count += 1
        print(count)

    def default(self, line):
        """called on input line when command prefix is not recognized.
        """
        args = line.split('.')
        command = args[1].split('(')[0]
        attrs = args[1].split('(')[1][:-1].replace(',', '').split()
        if attrs:
            attrs[0] = attrs[0][1:-1]
            if len(attrs) > 1:
                attrs[1] = attrs[1][1:-1]
        methods = {'all': self.do_all,
                   'count': self.do_count,
                   'show': self.do_show,
                   'destroy': self.do_destroy,
                   'update': self.do_update}
        for k, v in methods.items():
            if args[1][:len(k)] == k:
                v(args[0] + ' ' + ' '.join(attrs))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
