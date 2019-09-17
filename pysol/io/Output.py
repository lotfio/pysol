#  -*- coding: utf-8 -*-
#| This file is part of cony
#|
#| @package     pysol python cli application
#| @author      <lotfio lakehal>
#| @license     MIT
#| @version     0.1.0
#| @copyright   2019 lotfio lakehal

import sys

class Output:


    def __init__(self):
        pass

    # writeLine method
    # this method writes to the output
    # TODO::adding colors support
    def writeLn(self, line = '', color = 'white'):
        return sys.stdout.write(line)