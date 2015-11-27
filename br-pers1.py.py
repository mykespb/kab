#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# br-getpers1.py.py 2015-11-27 1.5
# get persons from web site bards.ru

import lxml.html as lh
from lxml.html import parse, tostring
#import requests
import pprint

PROG = "br-pers1.py"
VER  = "1.1"

URL  = "http://www.bards.ru"
PERS = URL + "/persons.php"


def get_letters ():
    """process base via parse"""
    doc = parse(PERS).getroot()
    doc.make_links_absolute()
    links = doc.xpath ("//td/*/a")
    letters = [(link.text, link.xpath('@href').pop()) for link in links]
    letters = [let for let in letters if 'persons' in let[1]]
    pprint.pprint (letters)
    #~ for letter in letters:
        #~ get_authors (letter)
    get_authors(letters[0])


def get_authors (loa):
    """get authors' names'"""
    leta, fname = loa
    print ("processing letter %s from file %s" % (leta, fname))
    try:
        doc = parse(fname).getroot()
        links = doc.xpath("//tr/td/table[@border=1]/tr")
        for link in links:
            #~ print (link)
            ref = link.xpath("td")
            #~ print (ref)
            a = ref[0].xpath("./a").pop()
            #~ print (tostring(a))
            href = a.xpath("@href")
            print ("href=", href.pop())
            desc = a.xpath('text()')
            print ("desc=", desc.pop())
            #~ a = ref[0].xpath("a")
            #~ print (a.xpath("@href").pop())
            #~ ref = link[0].xpath("./a")
            #~ print ("ref=", ref.text())
    except:
        print ("Cannot open file or error in file")


def main(args):
    """main dispatcher"""
    print ("This is %s ver. %s" % (PROG, VER))
    get_letters ()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

# http://bards.ru/persons.php?ch=%C0
# http://docs.python-guide.org/en/latest/scenarios/scrape/
# http://lxml.de/xpathxslt.html
# http://saxon.sourceforge.net/saxon6.5.3/expressions.html

