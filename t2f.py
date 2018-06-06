#!/usr/bin/python
# -*- coding: utf-8
#

import os
import sys
import argparse

PROG = os.path.basename(sys.argv[0]).rstrip('.py')
PROG_DESC = 'Convert template file to static'

def load_template(fname):
    read_data = ''
    if os.path.isfile(fname):
        with open(fname, 'r') as f:
            read_data = f.read()
            f.close()
    return read_data

def save(fname, save_data):
    with open(fname, 'w') as f:
        f.write(save_data)
        f.close()

class argReplace(object):
    def __init__(self, _config):
        super(argReplace, self).__init__()
        setattr(self, 'a', 'b')
        print self.a

def _trim(s):
    return(s.lstrip('"\' ').rstrip('"\' '))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=PROG_DESC)
    parser.add_argument('-t', '--template', help="Template file name. File vars: {VAR1} {VAR2}")
    parser.add_argument('-r', '--replace', help="\"VAR1='VAL1', VAR2='VAL2'\"")
    parser.add_argument('-o', '--outfile', help="Output file name")
    args = parser.parse_args()

    if args.template and args.replace:
        load_data = load_template(args.template)
        r_args = args.replace.split(',')
        _replace = {}
        for r_arg in r_args:
            (k, v) = r_arg.split('=')
            _replace[ _trim(k)] = _trim(v)
        new_data = load_data.format(**_replace)
        if args.outfile:
            save(args.outfile, new_data)
        else:
            save(args.template + '.out', new_data)
    else:
        parser.print_help()
