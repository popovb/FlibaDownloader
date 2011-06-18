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

import Probing
from HTMLParser import *

class FlibaHTMLParser (HTMLParser):
	def __init__ (self):
		HTMLParser.__init__ (self)
		self._FileList = []
		return

	def handle_starttag (self, tag, attrs):
		if tag != 'a':
			return
		for atr, val in attrs:
			if atr == 'href':
				self._FileList.append (val);
		return

	def parse (self, html):
		del self._FileList [0:len (self._FileList)]
		self.feed (html)
		self.close ()
		return self._converse ()

	def _converse (self):
		list_of_dict = []

		for filename in self._FileList:

			temp = {'FileName' : filename};
			temp.update ( {'FirstNum' : Probing.getFirstNum (filename)} )
			temp.update ( {'LastNum'  : Probing.getLastNum  (filename)} )
			temp.update ( {'Type'     : Probing.getType     (filename)} )
			list_of_dict.append (temp)
		return list_of_dict
