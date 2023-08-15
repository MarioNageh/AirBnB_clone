#!/usr/bin/env python3
"""This module contains the entry point of the command interpreter"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
