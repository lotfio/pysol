#  -*- coding: utf-8 -*-
#| This file is part of cony
#|
#| @package     pysol python cli application
#| @author      <lotfio lakehal>
#| @license     MIT
#| @version     0.1.0
#| @copyright   2019 lotfio lakehal

import sys

class Input:
    # @property command
    comm        = None

    # @property sub command
    sub_comm    = None

    # @property input options
    inp_options = []

    # @property flags
    inp_flags   = []

    # constructor method
    # when application is run this constructor captures
    # the input from argv and extract the array info
    # command, subcommand, options, flags
    # a command with colone will be spliced to command and sub commands
    def __init__(self):

        # remove file name
        sys.argv.pop(0)
        self.cmd = sys.argv

        if(self.cmd):

            if(":" in self.cmd[0]): # check if sub command

                comm = self.cmd[0].split(":")
                self.comm     = comm[0]
                self.sub_comm = comm[1]
                sys.argv.pop(0)
            else: # if not sub command get only command

                self.comm     = self.cmd[0]
                self.sub_comm = None
                sys.argv.pop(0)
        else:  # if no command no sub affect to None

            self.comm         = None
            self.sub_comm     = None

        ## capture options and flags
        if(sys.argv):
            for x in sys.argv:
                if (x.startswith('-')) or (x.startswith('--')):
                    self.inp_flags.append(x)
                else:
                    self.inp_options.append(x)

    # command method
    # returns input command
    def command(self):
        return self.comm

    # subcommand method
    # returns input subcommand
    def subcommand(self):
        return self.sub_comm

    # option method
    # returns input options as ana array
    def options(self):
        return self.inp_options

    # flags method
    # returns input flags as an array
    def flags(self):
        return self.inp_flags