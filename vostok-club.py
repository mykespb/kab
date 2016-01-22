#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (C) Mikhail (myke) Kolodin 2016-01-22 1.1
# convert downloaded vostok.tsv file to club.tab (utf8)

import csv

namein  = 'vostok.tsv'
nameout = 'club1.tab'

with open(namein) as filein, open(nameout, "wt") as fileout:
    r = csv.reader (filein, dialect="excel-tab")
    w = csv.writer (fileout, dialect="excel-tab")

    rownum = 0
    for row in r:
        rownum += 1
        if rownum == 1:
            header = row
            orow = "file\tfname\tpname\tlname\tsex\tbd\tduty".split()
            w.writerow (orow)
        else:
            orow = row[0], row[2], row[3], row[1], row[5], row[6], row[12]
            w.writerow (orow)

