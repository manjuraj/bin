#! /usr/bin/env python

import sys
import requests

url = str(sys.argv[1])
rsp = requests.get(url, timeout=5)
if rsp.ok:
  print rsp.text
