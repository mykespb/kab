#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# having folders with photos names acc to data&time
# we move them to subdirectories acc to month.
# no params needed
# myke 2013-09-18 1.1

import os, os.path, shutil

ver= '1.1'
print 'foto-movetosubdirs by myke ver.%s' % (ver,)

def proc (f):
	""" process one file """
        data = f[:10][:7]
	if not os.path.exists (data):
		print data,
		os.mkdir (data)
	shutil.move (f, data)

def main():
	""" main routine """
	
	#~ lof = os.listdir ('.')
	#~ print lof
	
	for f in os.listdir ('.'):
		if f.lower().endswith ('.jpg'):
			proc (f)
	
	return 0

if __name__ == '__main__':
	main()

