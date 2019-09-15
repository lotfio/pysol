#  -*- coding: utf-8 -*-
#| This file is part of cony
#|
#| @package     Pysol python cli application
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

    def __init__(self):
        # constructor method
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

    def command(self):
        # return input command method
        return self.comm

    def subcommand(self):
        # return input sub command method
        return self.sub_comm

    def options(self):
        # return input options method
        return self.inp_options

    def flags(self):
        # return input flags method
        return self.inp_flags