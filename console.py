#!/usr/bin/python3

"""
Creating a command line interpreter instance from class Cmd
"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import models


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter for HBNB."""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Help information for the quit command."""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()  # Print a newline for better formatting
        return True

    def emptyline(self):
        """
        Overriding the emptyline method
        """
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        instance = self.classes[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Show an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Print all string representation of all instances"""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return

        instances = storage.all()
        result = []
        for key, value in instances.items():
            if not arg or key.startswith(arg):
                result.append(str(value))
        print(result)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"')
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                print(f"** invalid value for {attr_name} **")
                return
            except TypeError:
                print(f"** can't update {attr_name} **")
                return
        try:
            setattr(instance, attr_name, attr_value)
            instance.save()
        except TypeError:
            print("TypeError: check your args again please")
            return

    def default(self, line):
        """Default method to handle unknown commands."""
        args = line.split(".")
        if len(args) == 2 and args[1] == "all()":
            class_name = args[0]
            if class_name in self.classes:
                self.do_all(class_name)
            else:
                print("** class doesn't exist **")
        else:
            print(f"*** Unknown syntax: {line}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
