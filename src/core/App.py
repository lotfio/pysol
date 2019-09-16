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

class App:

    def __init__(self, inp, out):
        #
        # constructor
        self.inp         = inp
        self.out         = out
        self.baseCommand = Command()

    def display_logo(self):
        #
        # display app logo

        f = open(cfg.logo_file)
        self.out.writeLn(f.read())

    def display_basic_info(self):
        #
        # display app basic info

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
                cmd.execute(self.inp.subcommand(), self.inp.options(), self.inp.flags())
                exit()

            else:
               self.out.writeLn("\n [ command "+ self.inp.command() +" not found ]\n")
               exit()

    def run(self):
        '''
        + run application
        '''
        self.bind_inp_out()
        self.display_logo()
        self.display_basic_info()
        self.baseCommand.available_commands()