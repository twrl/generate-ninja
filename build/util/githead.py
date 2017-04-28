#!/usr/bin/env python
import os
import re
from sys import argv, stderr

#dirname =
parts =  argv[1].rpartition("/.git")
print >> stderr, parts

if os.path.isfile(parts[0] + parts[1]):
  g = open(parts[0] + parts[1], 'r')
  gf = g.readline()
  g.close()
  gitdir = re.match('gitdir: (.*)', gf).group(1)
  if os.path.isabs(gitdir):
    dirname = gitdir
  else:
    dirname = os.path.normpath(os.path.join(parts[0], gitdir))
  headfile = os.path.normpath(dirname + parts[2])
else:
  headfile = argv[1]
  dirname = os.path.dirname(headfile)

print >> stderr, "headfile: " + headfile
print >> stderr, "gitdir: " + dirname


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
