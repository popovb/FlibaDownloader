#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

import re
from HTMLParser import *

def _get (filename, template):
	r = re.findall (template, filename)
	if len (r) == 0:
		return 0
	return r[0][1:len(r[0])-1]

def _getFirstNum (filename):
	return _get (filename, r"\.[0-9]+-")

def _getLastNum (filename):
	return _get (filename, r"-[0-9]+\.")

def _probe (filename, template):
	return re.search (template, filename)

def _probeNOFB2 (filename):
	return _probe (filename, r".+\.n\..+")

def _probeFB2 (filename):
	return _probe (filename, r".+fb2.+")

def _getType (filename):
	if _probeFB2 (filename):
		return 'FB2'
	if _probeNOFB2 (filename):
		return 'NO_FB2'
	return 'FB2'

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
			temp.update ( {'FirstName' : _getFirstNum (filename)} )
			temp.update ( {'LastName'  : _getLastNum  (filename)} )
			temp.update ( {'Type'      : _getType     (filename)} )
			list_of_dict.append (temp)
		return list_of_dict
