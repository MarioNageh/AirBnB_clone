#!/usr/bin/env python3
"""This module contains the entry point of the command interpreter"""
import cmd
import models
from models.user import User
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """This class contains the entry point of the command interpreter"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Exit the program"""
        return True

    def do_quit(self, line):
        """Exit the program"""
        return True

    def emptyline(self):
        """Empty line."""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in models.storage.CLASSES:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{line}()")
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation
        of an instance based on the class <name> and <id>
        """
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if len(args) == 1:
            print("** instance id missing **")
            return
        name = args[0]
        instance_id = args[1]
        if name not in models.storage.CLASSES:
            print("** class doesn't exist **")
            return

        key = name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class <name> and <id>"""
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if len(args) == 1:
            print("** instance id missing **")
            return
        name = args[0]
        instance_id = args[1]
        if name not in models.storage.CLASSES:
            print("** class doesn't exist **")
            return

        key = name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation
        of all instances based or not on the class name
        """
        args = line.split()
        class_name = None
        if len(args) == 1:
            class_name = args[0]

        if class_name not in models.storage.CLASSES and class_name is not None:
            print("** class doesn't exist **")
            return

        list_of_instances = []
        for key, value in models.storage.all().items():
            if not class_name:
                list_of_instances.append(value.__str__())
            elif value.__class__.__name__ == class_name:
                list_of_instances.append(value.__str__())

        print(list_of_instances)

    def do_update(self, line):
        """
            Updates an instance based on the class
            name and id by adding or updating attribute
            <class name> <id> <attribute name> "<attribute value>
        """

        if not line:
            print("** class name missing **")
            return

        args = line.split()
        name = args[0]
        if name not in models.storage.CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]

        data = models.storage.all()
        key = name + "." + instance_id
        if key not in data:
            print("** no instance found **")
            return
        object_instance = data[key]
        setattr(object_instance, attribute_name, eval(attribute_value))
        object_instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
