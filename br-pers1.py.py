#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# br-getpers1.py 2015-11-27 1.0
# get persons from web site bards.ru

import lxml.html as lh
from lxml.html import parse, tostring
#import requests
import pprint

PROG = "br-pers1.py"
VER = "0.1"

URL = "http://www.bards.ru"
PERS = URL + "/persons.php"

def get_letters ():
    """process base via parse"""
    doc = parse(PERS).getroot()
    doc.make_links_absolute()
    links = doc.xpath ("//td/*/a")
    letters = [(link.text, link.xpath('@href').pop()) for link in links]
    letters = [let for let in letters if 'persons' in let[1]]
    pprint.pprint (letters)

def main(args):
    """main dispatcher"""
    print ("This is %s ver. %s" % (PROG, VER))
    get_letters ()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
