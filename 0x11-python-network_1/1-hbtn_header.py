#!/usr/bin/python3
# This script that takes in a URL sends a request to the URL
import sys
from urllib import (request)

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as res:
        print(res.info()['X-Request-Id'])
