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

from flibaloader.FlibaLoader          import *
from flibaloader.FlibaDailyPageParser import *
from flibaloader.FlibaLocalDir        import *
from flibaloader.ListGenerator        import *

#TODO try to exception

daily_page = getDailyPage ()
parser = FlibaHTMLParser ()
file_list_in_flibusta  = parser.parse (daily_page)
#print file_list_in_flibusta

local_dir = FlibaLocalDir ();
content = local_dir.getContentDir ('/media/toshiba2/boris/fb2.Flibusta.Net/')
#print content
#print len (content)
list_for_download = getList_FB2 (content, file_list_in_flibusta)
print list_for_download

	
#TODO
