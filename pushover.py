#!/usr/bin/env python

import urllib
import urllib2
import urlparse
import json
import argparse
import os

PUSHOVER_API = "https://api.pushover.net/1/"

class PushoverError(Exception): pass

def pushover(**kwargs):
    assert 'message' in kwargs

    if not 'token' in kwargs:
        kwargs['token'] = os.environ['PUSHOVER_TOKEN']
    if not 'user' in kwargs:
        kwargs['user'] = os.environ['PUSHOVER_USER']

    url = urlparse.urljoin(PUSHOVER_API, "messages.json")
    data = urllib.urlencode(kwargs)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    output = response.read()
    data = json.loads(output)

    if data['status'] != 1:
        raise PushoverError(output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Send Pushover.net message")
    parser.add_argument('message', 
            type=str,
            help="Message to send",
            )
    parser.add_argument('--token',
            type=str,
            help="Pushover app token (overrides environment PUSHOVER_TOKEN)",
            )
    parser.add_argument('--user',
            type=str,
            help="Pushover user key (overrides ",
            )
    parser.add_argument('--title',
            type=str,
            help="Message title",
            )
    parser.add_argument('--timestamp',
            type=int,
            help="Optional UNIX timestamp",
            )
    parser.add_argument('--priority',
            type=int,
            help="Optional priority setting (0=normal, 1=high)",
            default=0,
            )
    args = parser.parse_args()

    d = {}
    for k, v in vars(args).iteritems():
        if v: d[k] = v

    pushover(**d)
