#  -*- coding: utf-8 -*-
#| This file is part of cony
#|
#| @package     Pysol python cli application
#| @author      <lotfio lakehal>
#| @license     MIT
#| @version     0.1.0
#| @copyright   2019 lotfio lakehal

import os.path
import sys
import src.cfg.app as cfg
from   src.core.Command import Command
from   src.core.helpers import load_module
from   src.exceptions.CommandNotFoundException import CommandNotFoundException

class App:

    # constructor method
    # setting input + output + base command
    def __init__(self, inp, out):
        self.inp         = inp
        self.out         = out
        self.baseCommand = Command(inp, out)

    # bind input output method
    # this method checks if a command exists and it is
    # a module then it will instantiate it and execute it
    def bind_inp_out(self):
        #
        # bind inp to command and return output
        #
        comm = self.inp.command()

        if(comm):
            f = cfg.root + "/commands/" + comm.lower() + ".py"

            if os.path.isfile(f):

                a       = load_module("src.commands." + comm)
                command = getattr(a, comm)
                cmd     = command(self.inp, self.out)
                exit(
                    cmd.execute(self.inp.subcommand(), self.inp.options(), self.inp.flags())
                )
            else:
               raise CommandNotFoundException("command "+comm + " not found")

    # run application
    def run(self):
        try:
            self.bind_inp_out()
            self.baseCommand.display_logo()
            self.baseCommand.display_basic_info()
            self.baseCommand.available_commands()
        except Exception as ex:
            err  = "\n => " + str(ex.__class__.__name__) + " :\n"
            err += "   - "  + str(ex)
            exit(err)