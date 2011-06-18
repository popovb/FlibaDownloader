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
import re
import Probing

def _probeFB2Arch (filename):
	template = r".+[0-9]+-[0-9]+.+";
	return re.search (template, filename)

class FlibaLocalDir:
	def __init__ (self):
		self._LocalDir = []
		return

	def getContentDir (self, localdir):
		del self._LocalDir [0 : len (self._LocalDir)]
		temp = os.listdir (localdir)

		for fn in temp:
			if _probeFB2Arch (fn):
				self._LocalDir.append (fn)
		
		return self._converse ()

	def _converse (self):
		list_of_dict = []

		for filename in self._LocalDir:

			temp = {'FileName' : filename};
			temp.update ( {'FirstNum' : Probing.getFirstNum (filename)} )
			temp.update ( {'LastNum'  : Probing.getLastNum  (filename)} )
			temp.update ( {'Type'     : Probing.getType     (filename)} )
			list_of_dict.append (temp)
		return list_of_dict
