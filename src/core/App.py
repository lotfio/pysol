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

    # display logo method
    # displays logo
    def display_logo(self):
        f = open(cfg.logo_file)
        self.out.writeLn(f.read())

    # display basic information
    # this method shows basic info
    def display_basic_info(self):
        info  = "\nWelcome to " + cfg.app_name + ' ' + cfg.app_version + ' by ' + cfg.app_author + '\n'
        info += "\nUsage : \n"
        info += "\n command:subcommand [options] [--flags] \n"
        info += "\nOptions, flags : \n"
        info += "\n -h, --help              Display help or command help \n"
        info += " -q, --quiet             Do not out any message \n"
        info += " -V, --version           Display application version \n"
        info += "     --ansi              Force ANSI output \n"
        info += "     --no-ansi           Disable ANSI output \n"
        info += " -n, --no-interaction    Do not ask any interactive question \n"
        info += "     --profile           Display timing and memory usage information \n"
        info += "     --no-plugins        Whether to disable plugins. \n"
        info += "     --no-cache          Prevent use of the cache \n"

        self.out.writeLn(info)

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
            self.display_logo()
            self.display_basic_info()
            self.baseCommand.available_commands()
        except Exception as ex:
            err  = "\n => " + str(ex.__class__.__name__) + " :\n"
            err += "   - "  + str(ex)
            exit(err)