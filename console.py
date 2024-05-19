#!/usr/bin/python3

"""
Creating a command line interpreter instance from class Cmd
"""


import cmd
import os
import re
from models import the_file_storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def parse_arguments(arg: str) -> list:
    """Splits a string into tokens based on delimiters."""
    return re.split(r"[ .(),]", arg)


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter for HBNB."""

    prompt = "(hbnb) "
    SUPPORTED_CLASSES = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review",
    }

    def do_quit(self, arg: str) -> bool:
        """Exit the program."""
        return True

    def do_EOF(self, arg: str) -> bool:
        """Handle EOF to exit the program."""
        print()
        return True

    def emptyline(self):
        """Override the emptyline method to do nothing."""
        pass

    def default(self, arg: str):
        """Handle unrecognized commands."""
        method_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
        }
        tokens = parse_arguments(arg)
        if len(tokens) < 2:
            print("*** Unknown syntax: {}".format(arg))
            return

        class_name, action = tokens[0], tokens[1]
        if action not in method_map:
            print("*** Unknown syntax: {}".format(arg))
            return

        if action in ["all", "count"]:
            method_map[action](class_name)
        elif len(tokens) >= 3:
            instance_id = tokens[2].strip('"')
            if action == "show" or action == "destroy":
                method_map[action]("{} {}".format(class_name, instance_id))
            elif action == "update":
                if len(tokens) == 4:
                    attr_name = tokens[3].strip('"')
                    method_map[action](
                        "{} {} {}".format(class_name, instance_id, attr_name)
                    )
                elif len(tokens) > 4:
                    attr_name = tokens[3].strip('"')
                    attr_value = tokens[4].strip('"')
                    method_map[action](
                        "{} {} {} {}".format(
                            class_name, instance_id, attr_name, attr_value
                        )
                    )
        else:
            print("*** Unknown syntax: {}".format(arg))

    def do_create(self, arg: str):
        """Create a new instance of a class."""
        if not arg:
            print("** class name missing **")
            return

        class_name = parse_arguments(arg)[0]
        if class_name not in self.SUPPORTED_CLASSES:
            print("** class doesn't exist **")
            return

        instance = eval(class_name)()
        instance.save()
        print(instance.id)

    def do_show(self, arg: str):
        """Display the string representation of an instance."""
        tokens = parse_arguments(arg)
        if len(tokens) < 1:
            print("** class name missing **")
            return

        class_name = tokens[0]
        if class_name not in self.SUPPORTED_CLASSES:
            print("** class doesn't exist **")
            return

        if len(tokens) < 2:
            print("** instance id missing **")
            return

        instance_id = tokens[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = the_file_storage.all()
        if key not in all_objs:
            print("** no instance found **")
        else:
            print(all_objs[key])

    def do_destroy(self, arg: str):
        """Delete an instance based on class name and id."""
        tokens = parse_arguments(arg)
        if len(tokens) < 1:
            print("** class name missing **")
            return

        class_name = tokens[0]
        if class_name not in self.SUPPORTED_CLASSES:
            print("** class doesn't exist **")
            return

        if len(tokens) < 2:
            print("** instance id missing **")
            return

        instance_id = tokens[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = the_file_storage.all()
        if key in all_objs:
            del all_objs[key]
            the_file_storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg: str):
        """Print all string representations of all instances."""
        tokens = parse_arguments(arg)
        all_objs = the_file_storage.all()
        if len(tokens) == 0:
            print([str(obj) for obj in all_objs.values()])
        else:
            class_name = tokens[0]
            if class_name in self.SUPPORTED_CLASSES:
                print([str(obj) for key, obj in all_objs.items() if key.startswith(class_name)])
            else:
                print("** class doesn't exist **")

    def do_update(self, arg: str):
        """Update an instance by adding or updating an attribute."""
        tokens = parse_arguments(arg)
        if len(tokens) < 1:
            print("** class name missing **")
            return

        class_name = tokens[0]
        if class_name not in self.SUPPORTED_CLASSES:
            print("** class doesn't exist **")
            return

        if len(tokens) < 2:
            print("** instance id missing **")
            return

        instance_id = tokens[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objs = the_file_storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return

        if len(tokens) < 3:
            print("** attribute name missing **")
            return

        if len(tokens) < 4:
            print("** value missing **")
            return

        obj = all_objs[key]
        attr_name = tokens[2]
        attr_value = tokens[3]

        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            setattr(obj, attr_name, attr_type(attr_value))
        else:
            setattr(obj, attr_name, attr_value)
        obj.save()

    def do_count(self, arg: str):
        """Count the number of instances of a class."""
        tokens = parse_arguments(arg)
        if tokens[0] in self.SUPPORTED_CLASSES:
            class_name = tokens[0]
            count = sum(
                1 for key in the_file_storage.all().keys() if key.startswith(class_name)
            )
            print(count)
        else:
            print("** class doesn't exist **")

    def do_clear(self, arg: str):
        """Clear the console screen."""
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
