#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# mk-mkmeet.py 2016-01-06 2016-01-06 1.0
# (C) Mikhail Kolodin, 2016
# format bards songs file with simplest markdown into web page for easy searching and singing
# makes only 1 column
# call:    mk-mkmeet.py file.txt
# result:  file.html (all in one)

import sys, pprint

# version
ver = '1.0'
adate = '2016-01-06'

COLS = 1    # only 1 column!

inname = outname = None
#inname  = "all-2015fall.txt"
#outname = "all-2015fall.html"

#index
index = []   # all songs list
snum = 0     # song number
title = ""   # file title

def main():
    """ main fun """
    global inname, outname
    print ("This is mk-mkmeet.py")
    inname = inname or sys.argv[1]
    if not inname:
        print ("No good file name. Quitting.")
    else:
        if inname[-4:] == ".txt":
            outname = inname[:-4] + ".html"
        else:
            outname = inname + ".html"
        print ("Inname=%s, outname=%s.\nStarting." % (inname, outname))
        pass1()
        pass2()

def pass1 ():
    """collect index"""
    global inname, outname, index, snum, title
    full = ""
    print ("pass 1: making index")
    with open (inname) as infile:
        was = ""
        for line in infile:
            if line.startswith("===="):
                # we have file title
                title = was.strip()
                print ("file: %s" % (title,))
                continue

            if line.startswith("----"):
                # we have song title
                full = was.strip()
                print ("song: %s." % (full,))
                snum += 1
                #~ index.append([snum, author, name, 0])
                index.append([snum, full, 0])
                continue

            # normal line
            if index:
                index[-1][-1] += 1
            was = line

def pass2 ():
    """output result"""
    global inname, outname, index, snum, title
    full = ""
    print ("pass 2: making html")
    pprint .pprint (index)

    index.sort (key=lambda x: x[1:])

    with open (outname, 'w') as outfile:
        print ("""<!DOCTYPE HTML>
<html lang='ru'>
<head>
<meta encoding=utf8>
<meta http-equiv = "content-type" content = "text/html; charset = utf-8">
<meta name="keywords" content="mikhail kolodin, bards, song, author, st.petersburg, колодин, авторская песня, барды, parties">
<meta name="description" content="mikhail kolodin bards song parties">
<title>%s</title>
<!-- program mk-mkmeet.py ver. %s of %s (C) Mikhail Kolodin -->
</head>
<body>
<h1>%s</h1>

""" % (title, ver, adate, title), file=outfile)

        print ("<a name='0'>", file=outfile)
        print ("\n<div><table frame=void rules=cols cellpadding=5mm ><tr>", file=outfile)
        for onum, song in enumerate(index):
            #~ if onum % 90 == 0:
                #~ print ("\n</td></tr></table></div>\n\n<div><table frame=void rules=cols cellpadding=5mm ><tr>", file=outfile)
            #~ if onum % 30 == 0:
                #~ print ("\n<td align=left valign=top>\n", file=outfile)
            anum, afull, alen = song
            print ("<div align=left valign=top><a href='#%d'>%03d. %s.</a> (%d)</div>" % (anum, anum, afull, alen), file=outfile)
        print ("\n</tr></table>\n</div>\n<br/ >\n", file=outfile)

        snum = 0
        row = 0
        with open (inname) as infile:
            was = wass = ""
            cwas = 0
            dout = 0
            for line in infile:
                if line.startswith("===="):
                    # we have file title
                    dout = 0
                    title = was.strip()
                    print ("file: %s" % (title,))
                    continue

                if line.startswith("----"):
                    # we have song title
                    dout = 1
                    full = was.strip()
                    print ("song: %s." % (full,))
                    snum += 1
                    if snum>1:
                        print ("\n</pre>\n</td></tr>\n</table>\n", file=outfile)
                    print ("\n<a href='#0'>К началу...</a>\n<hr>\n", file=outfile)
                    print ("<a name='%d'>" % (snum,), file=outfile)
                    print ("<p><b>%s.</b></p>" % (full,), file=outfile)

                    print ("\n<div>\n<table border=0 frame=void rules=cols cellpadding=5mm  ><tr><td align=left valign=top cellpadding=5mm>", file=outfile)
                    row = 0
                    cwas = 1

                    print ("\n<pre>", file=outfile)
                    continue

                if dout == 1:
                    dout = 2

                # normal line: pass
                if dout > 1 and (wass != title and wass != full):
                    if wass != "" or cwas == 0:
                        print (was, file=outfile, end="")
                        dout = 3
                        row += 1
                        #~ if row == 30:
                            #~ row = 0
                            #~ print ("</pre></td><td align=left valign=top cellpadding=5mm><pre>", file=outfile)
                            #~ cwas = 1

                    if was.strip() == "":
                        cwas += 1
                    else:
                        cwas = 0

                elif dout >2 :
                    print (was, file=outfile, end="")

                # end of line
                was = line
                wass = was.strip()

        print ("""
</pre>
</table>
<a href='#0'>К началу...</a>\n<hr>
</body>
</html>
""", file=outfile)

# call 'em
main()

# details.

#~ input file format:

#~ name of meetimg
#~ =========================

#~ author's name and surname. song name
#~ -------------------------------------

#~ text of song (out as <pre>)
#~ ...

#~ output contains contents part first

#~ all data are in utf-8 !

# TBD: don't cut inside couplets, if possible.
