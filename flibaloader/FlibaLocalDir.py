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

import os

class FlibaLocalDir:
	def __init__ (self, localdir):
		self._LocalDir = localdir
		return;

	def getLastNumberFB2 (self):
		#TODO
		temp = os.listdir (self._LocalDir)

		#TODO
		return temp
	
	def getLastNumberNO_FB2 (self):
		#TODO
		return []
