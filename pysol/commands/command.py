#  -*- coding: utf-8 -*-
#| This file is part of cony
#|
#| @package     pysol python cli application
#| @author      <lotfio lakehal>
#| @license     MIT
#| @version     0.1.0
#| @copyright   2019 lotfio lakehal

import os
import pysol.conf.app as cfg
from   pysol.core.Command import Command as baseCommand


class command(baseCommand):

    # comand description
    description = 'This command helps you to create, delete and update commands'

    # execute method
    # this method is where your sub commands and flags should be
    # executed
    def execute(self, sub = None, options = [], flags = []):

        # This method should execute our commands
        if(sub):
            if(sub == 'make'):
                return self.make(options)
            elif(sub == 'delete'):
                return self.remove(options)
            else:
                return self.no_sub_command(sub)

        return self.help()


    # Make method
    # This method creates a command based on the given name
    def make(self, options):

        if not options: # not name
            raise RuntimeError("please enter a command name that you want to create")

        name = options[0] #command name

        f = cfg.root + "/commands/" + name.lower() + ".py"
        # check if already exists
        if os.path.isfile(f):
            raise RuntimeError("command "+ name + " already exists")

        # create command
        stub =  cfg.root + "/commands/cmd.stub"
        cmd  =  cfg.root + "/commands/" + name + ".py"

        # create a command from stub file
        with open(stub, "rt") as fin:
            with open(cmd, "wt") as fout:
                for line in fin:
                    fout.write(line.replace('#class#', name))

        return self.out.writeLn("\n command " + name + " has been created successfully \n")

    # delete command method
    # this method will delete command files
    # based on the given name of course if exists in commands dir
    def remove(self, options):

        if not options: # not name
            raise RuntimeError("please enter a command name that you want to delete")

        name = options[0] #command name

        f = cfg.root + "/commands/" + name.lower() + ".py"
        # check if already exists
        if os.path.isfile(f):
            os.remove(f)
            return self.out.writeLn("\n command "+name+" has been deleted successfully \n")
        else:
            raise RuntimeError("command "+ name + " doesn't exist")


    # help method
    # This method displays command help
    def help(self):

        msg = "   This is a build in command\n   This command helps you to create and delete other commands \n\n"
        sub = {
            "make"   : "This is make command",
            "delete" : "This is delete command"
        }
        options = {}
        flags   = {}
        return  self.command_help(self.__class__.__name__, msg, sub, options, flags)