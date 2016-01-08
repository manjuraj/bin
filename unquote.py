#! /usr/bin/env python

import sys
import urllib

from pprint import pprint

if len(sys.argv) == 2:
    line = str(sys.argv[1])
else:
    line = sys.stdin.read()

unquoted = urllib.unquote(line)
for line in unquoted.split():
    pprint(line.split("&"))
