#!/usr/bin/python3


"""
    Cmd => command line interfaces

    Creating a command line interpreter instance from class Cmd
"""
import cmd
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import the_file_storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the HBNB project."""

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

    def do_quit(self, _):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, _):
        """EOF command to exit the program."""
        print()  # Print a newline for better formatting
        return True

    def emptyline(self):
        """
        Overriding the emptyline method

        to disable the repetition of the last command,

        Do nothing on empty input line.
        """

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
        instance = the_file_storage.all().get(key)
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
        if key not in the_file_storage.all():
            print("** no instance found **")
            return
        del the_file_storage.all()[key]
        the_file_storage.save()

    def do_all(self, arg):
        """Print all string representation of all instances
        based or not on the class name."""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return

        instances = the_file_storage.all()
        result = []
        for key, value in instances.items():
            if not arg or key.startswith(arg):
                result.append(str(value))
        print(result)

    def do_update(self, arg):
        """
        Update an instance based on the
        class name and id by adding or updating attribute.
        """
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
        instance = the_file_storage.all().get(key)
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

    # def do_clear(self, arg):
    #     """
    #     Clear the console screen

    #     Not Required method for project
    #     """
    #     os.system("cls")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
