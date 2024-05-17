#!/usr/bin/python3


"""
    Console entry point
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the HBNB project."""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()  # Print a newline for better formatting
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
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
        """Print all string representation of all instances based or not on the class name."""
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
        """Update an instance based on the class name and id by adding or updating attribute."""
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
        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
