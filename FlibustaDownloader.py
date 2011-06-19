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

import sys
import getopt
from flibaloader.FlibaLoader          import *
from flibaloader.FlibaDailyPageParser import *
from flibaloader.FlibaLocalDir        import *
from flibaloader.ListGenerator        import *
from flibaloader.Downloader           import *

PROGRAMM = 'FlibustaDownloader.py'
VERSION = '0.1.1'
LOCAL_PATH = ''

def info ():
	print PROGRAMM + ", ver." + str (VERSION)
	print """Copyright (c) 2011, Boris Popov <popov.b@gmail.com>
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
	return

def help ():
	info ()
	print "Usage: " + PROGRAMM + """ [OPTIONS]
       -h      display this usage message;
       -d dir  local directory.
"""
	return

try:
	opts, args = getopt.getopt (sys.argv[1:], 'd:h')

except getopt.GetoptError:
	print >> sys.stderr, "Error of command line!"
	sys.exit (1)

for arg, val in opts:

	if arg == '-h':
		help ()
		sys.exit (0)
		
	elif arg == '-d':
		LOCAL_PATH = val
		
try:
	daily_page = getDailyPage ()

except:
	print >> sys.stderr, "Error of retrieving remote filelist!"
	print >> sys.stderr, "Maybe flibusta is down..."
	print >> sys.stderr, "Please, check your computer's network connection, firewall, proxy, etc..."
	sys.exit (2)

parser = FlibaHTMLParser ()
file_list_in_flibusta  = parser.parse (daily_page)

local_dir = FlibaLocalDir ();

try:
	content = local_dir.getContentDir (LOCAL_PATH)

except:
	print >> sys.stderr, "Error of retrieving local filelist!"
	print >> sys.stderr, "Please, check option -d."
	sys.exit (6)
	
list_for_download = getList_FB2 (content, file_list_in_flibusta)

sys.exit ( downloadFiles (list_for_download, LOCAL_PATH) )
