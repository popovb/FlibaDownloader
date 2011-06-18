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

def _isItRangeNum (remotefile, locallist, typef):
	SUCCESS = True
	FAULT = False

	for localfile in locallist:
		if localfile['Type'] == typef:
			if remotefile['FirstNum'] >= localfile['FirstNum']:
				if remotefile['LastNum'] <= localfile['LastNum']:
					return SUCCESS
	return FAULT

def getList_FB2 (locallist, remotelist):
	mylist = []
	if len (remotelist) == 0:
		return mylist

	for remotefile in remotelist:
		if remotefile['Type'] == 'NO_FB2':
			continue

		if remotefile in locallist:
			continue

		if not _isItRangeNum (remotefile, locallist, 'FB2'):
			mylist.append (remotefile['FileName'])

	return mylist

def getList_NOFB2 (locallist, remotelist):
	mylist = []
	if len (remotelist) == 0:
		return mylist

	for remotefile in remotelist:
		if remotefile['Type'] == 'FB2':
			continue

		if remotefile in locallist:
			continue

		if not _isItRangeNum (remotefile, locallist, 'NO_FB2'):
			mylist.append (remotefile['FileName'])

	return mylist
