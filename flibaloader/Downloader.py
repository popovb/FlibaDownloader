#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2011, Boris Popov <popov.b@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>. 

import os
import sys
import urllib2

BASE_ADDRESS1 = 'http://www.flibusta.net/daily/'
BASE_ADDRESS2 = 'http://proxy.flibusta.net/daily/'
TIMEOUT = 10

def _getX (address):
	response = urllib2.urlopen (address, None, TIMEOUT)
	return response.read ()

def getDailyPage ():
	try:
		rp = _getX (BASE_ADDRESS1)
	except:
		rp = _getX (BASE_ADDRESS2)
	return rp

def getFileContent (FileName):
	try:
		rp =  _getX (BASE_ADDRESS1 + FileName)
	except:
		rp =  _getX (BASE_ADDRESS2 + FileName)
	return rp

def downloadFiles (filelist, download_dir):
	for fn in filelist:
		remotename = os.path.join (BASE_ADDRESS1, fn)
		print "Download " + remotename + " ...",
		sys.stdout.flush ()
	
		###
		try:
			content = getFileContent (fn)

		except:
			print >> sys.stderr, "Error of downloading file!"
			return 3;
		###

		myfilename = os.path.join (download_dir, fn)
		
		###
		try:
			fh = open (myfilename, "wb")

		except:
			print >> sys.stderr, "Error of opening file!"
			return 4;
		###

		###
		try:
			fh.write (content)

		except:
			print >> sys.stderr, "Error of saving file!"
			fh.close ()
			return 5;
		###
		
		print "OK"
		sys.stdout.flush ()
		fh.close ()
	return 0
