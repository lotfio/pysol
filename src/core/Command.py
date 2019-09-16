#  -*- coding: utf-8 -*-
#| This file is part of cony
#|
#| @package     Pysol python cli application
#| @author      <lotfio lakehal>
#| @license     MIT
#| @version     0.1.0
#| @copyright   2019 lotfio lakehal

import glob, os
from src.cfg.app import root
from src.core.helpers import load_module
from src.exceptions.SubCommandNotFoundException import SubCommandNotFoundException

class Command:

    # @var available commands
    avail_commands = {}

    # constructor
    # setting input and output
    def __init__(self, inp, out):
        self.inp = inp
        self.out = out

    # no sub command method
    # return no command found
    def no_sub_command(self, sub):
        raise SubCommandNotFoundException("sub command " + sub + " not found")

    # available commands method
    # list and display all commands and there description
    def available_commands(self):

        print("\nAvailable commands :\n")
        os.chdir(root + "/commands/")

        for file in glob.glob("*.py"):

            f = file.split(".")[0]
            m = load_module("src.commands."+f)
            c = getattr(m, f)
            self.avail_commands[f] = c.description

        ## tallest command
        t = len(max(self.avail_commands, key=len))

        for com in self.avail_commands:

            ad   = 4 if t > 20 else 17 ## if taller than 20 characters use 4 spaces only else use 17
            wsp  = ((t - len(com) + ad)) ## number of white spaces for each command
            line = " " + com + (wsp * ' ') + self.avail_commands[com] + "\n" # format line with white spaces
            self.out.writeLn(line) # print line

    # This is the help command method
    # This method formats how command help should look
    # This method should be called in all commands
    # In case of help change update this method as it fits
    def command_help(self, command, msg, sub, options, flags):

        hp  = "\n=| "+ command +" |=\n\n"
        hp += msg
        hp += "=| sub commands |=\n\n"

        if(not sub):
            hp += "  There is no sub commands for this command\n"
        else:
            t    = len(max(sub, key=len))
            ad   = 8
            for i in sub:
                hp += " " * 3 + "> " + i +  ((t - len(i) + ad) * ' ')  + ":  " + sub[i] + "\n"

        hp  += "\n=| options |=\n\n"

        if(not options):
            hp += "   There is no options for this command\n"
        else:
            for i in options:
                hp += i

        hp  += "\n=| flags |=\n\n"

        if(not flags):
            hp += "   There is no flags for this command\n"
        else:
            for i in flags:
                hp += i

        return self.out.writeLn(hp)
