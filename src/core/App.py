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
from   src.cfg.app import *

class App:

    def __init__(self, inp, output):
        #
        # constructor
        #

        self.input  = inp
        self.output = output

    def display_logo(self):
        #
        # display app logo
        #

        f = open(logo_file)
        self.output.writeLn(f.read())

    def display_basic_info(self):
        #
        # display app basic info
        #
        info  = "\nWelcome to " + app_name + ' ' + app_version + ' by ' + app_author + '\n'
        info += "\nUsage : \n"
        info += "\n command:subcommand [options] [--flags] \n"
        info += "\nOptions, flags : \n"
        info += "\n -h, --help              Display help or command help \n"
        info += " -q, --quiet             Do not output any message \n"
        info += " -V, --version           Display application version \n"
        info += "     --ansi              Force ANSI output \n"
        info += "     --no-ansi           Disable ANSI output \n"
        info += " -n, --no-interaction    Do not ask any interactive question \n"
        info += "     --profile           Display timing and memory usage information \n"
        info += "     --no-plugins        Whether to disable plugins. \n"
        info += "     --no-cache          Prevent use of the cache \n"

        self.output.writeLn(info)


    def bind_inp_out(self):
        #
        # bind input to command and return output
        #
        comm = self.input.command()

        if(comm):
            f = root + "/commands/" + comm.lower() + ".py"

            if os.path.isfile(f):

                a = self.load_module("src.commands." + comm)
                command = getattr(a, comm)
                cmd = command()
                cmd.execute(self.input.subcommand(), self.input.options(), self.input.flags())
                exit()

            else:
               self.output.writeLn("\n [ command "+ self.input.command() +" not found ]\n")
               exit()

    def load_module(self, module):
        #
        # module_path = "mypackage.%s" % module
        #
        module_path = module

        if module_path in sys.modules:
            return sys.modules[module_path]

        return __import__(module_path, fromlist=[module])


    def run(self):
        '''
        + run application
        '''
        self.bind_inp_out()
        self.display_logo()
        self.display_basic_info()