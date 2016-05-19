#! /usr/bin/python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('value',help = 'show 2 * value',type = int)

args = parser.parse_args()

print args.value *2

