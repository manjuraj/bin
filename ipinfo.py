#! /usr/bin/env python

#
# Example:
# $ ipinfo.py 75.101.154.97
#
#  {
#    "ip": "75.101.154.97",
#    "hostname": "ec2-75-101-154-97.compute-1.amazonaws.com",
#    "city": "Ashburn",
#    "region": "Virginia",
#    "country": "US",
#    "loc": "39.0437,-77.4875",
#    "org": "AS14618 Amazon.com, Inc.",
#    "postal": "20147"
#  }

import sys
import requests

ip = str(sys.argv[1])
url = 'http://ipinfo.io/%s' % ip
headers = { 'User-Agent': 'curl/7.37.1' }
rsp = requests.get(url, headers=headers, timeout=5)
if rsp.ok:
  print rsp.content
