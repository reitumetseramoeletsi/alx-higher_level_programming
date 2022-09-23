#!/usr/bin/python3
"""
This script take in a URL, send a request to URL, and dispaly body
"""

import sys
from urllib import (request, error)

if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except error.URLError as e:
        print("Error code: {}".format(e.code))
