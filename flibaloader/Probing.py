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

import re

def _get (filename):
	template = r"[0-9]+-[0-9]+\."
	r = re.findall (template, filename)
	if (len (r) == 0):
		return [0, '0.']
	return re.split (r"-", r[0])

def getFirstNum (filename):
	return _get (filename) [0]

def getLastNum (filename):
	temp = _get (filename)
	return temp[1] [0:len(temp[1]) - 1]

def _probe (filename, template):
	return re.search (template, filename)

def _probeNOFB2 (filename):
	return _probe (filename, r".+\.n\..+")

def _probeFB2 (filename):
	return _probe (filename, r".+fb2.+")

def getType (filename):
	if _probeFB2 (filename):
		return 'FB2'
	if _probeNOFB2 (filename):
		return 'NO_FB2'
	return 'FB2'
