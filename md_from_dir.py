#!/bin/python3

import os
import sys


def format_list():
    for f in os.listdir(sys.argv[1]):
        if not f.startswith('.'):
            l_name = os.path.splitext(f)
            print('  - ' + '[' + str(l_name[0]) + '](' + './' + f + ')')

format_list()
