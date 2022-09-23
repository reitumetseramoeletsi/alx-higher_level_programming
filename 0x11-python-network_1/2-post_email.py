#!/usr/bin/python3
# This script take in URL and email and sends a POST request to the URL
import sys
from urllib import (request, parse)

if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('utf-8')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
