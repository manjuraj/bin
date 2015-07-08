#! /usr/bin/env python

import sys
import requests

url = str(sys.argv[1])
rsp = requests.get(url, timeout=None)
if rsp.ok:
    print rsp.content
else:    
    print "error: %s - %s: %s" %(rsp.status_code, rsp.reason, rsp)
