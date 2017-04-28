#!/usr/bin/env python
import os
import re
from sys import argv

dirname = os.path.dirname(argv[1])
parts = dirname.partition("/.git")
if os.path.isfile(parts[0] + parts[1]):
  g = open(parts[0] + parts[1], 'r')
  gitdir = g.readline()
  g.close()
  gmatch = re.match('gitdir: (.*)', gitdir)
  dirname = os.path.normpath(os.path.join(parts[0], gmatch.group(1)))
  headfile = os.path.join(dirname, parts[2])
else:
  headfile = argv[1]
  dirname = os.path.dirname(headfile)



f = open(headfile, 'r')
head = f.readline()
f.close()
match = re.match('ref: (.*)', head)
if match and os.path.isfile(dirname + "/" + match.group(1)):
  print match.group(1)
elif match:
  print "packed-refs"
else:
  print ""
