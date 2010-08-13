#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2010 Sagar Chalise <sagar@desktop>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import os,sys
mypath= os.path.join(os.path.dirname(os.path.abspath(__file__)),'database')
from buzhug import Base
db=Base(mypath)
db.create(('Words',str),('Speech',str),('Meaning',str),('Synonym',str),('Antonym',str),('English',str),mode='override')
db.open()
db.insert('/data to be inserted')
#Example db.insert('गरिब','विशेषणपद','धन सम्पति नभएको, दरिद्र, पैसा नभएको',None,'धनि','poor')
db.close()


