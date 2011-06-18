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

import FlibaLoader
import os

def downloadFiles (filelist, download_dir):
	for fn in filelist:
		remotename = os.path.join (FlibaLoader.BASE_ADDRESS, fn)
		print "Download " + remotename + " ",
		content = FlibaLoader.getFileContent (fn)
		myfilename = os.path.join (download_dir, fn)
		fh = open (myfilename, "w")
		fh.write (content)
		print "OK"
		fh.close ()
	return
