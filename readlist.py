#!/usr/bin/python

import sys
import re

lines = sys.stdin.readlines()

lines = [ l.strip() for l in lines ]

for line in lines:
    gem_name = re.search('^[^ ]+', line)
    gem_name = gem_name.group(0)

    versions_str = re.search('\((.*)\)', line)
    versions = [ v.strip() for v in versions_str.group(1).split(',') ]

#    for v in versions:
#        print 'gem install %s --version %s --ignore-dependencies' % (gem_name, v)
