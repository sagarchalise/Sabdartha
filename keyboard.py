#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       keylt.py
#       
#       Copyright 2009 Sagar Chalise <sagar@reddevil>
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


class Keyboard():
	def GetNepKey(self,key):
		if key==46 or key==48 or key==49 or key==50 or key==51 or key==52 or key==53 or key==54 or key==55 or key==56 or key==57 or key==58 or key==59:
			key=key+2358
			return key
		elif key==47:
			key=key+2334
			return key
		elif key==60 or key==96 or key==97:
			key=key+2269
			return key
		elif key==62:
			key=key+2343
			return key
		elif key==65 or key==89 or key==115:
			key=key+2245
			return key
		elif key==66:
			key=key+2283
			return key
		elif key==67:
			key=key+2263
			return key
		elif key==68 or key==83:
			key=key+2275
			return key
		elif key==69:
			key=key+2307
			return key
		elif key==70 or key==79:
			key=key+2244
			return key
		elif key==71 or key==84 or key==104:
			key=key+2257
			return key		
		elif key==72 or key==87 or key==122:
			key=key+2237
			return key
		elif key==73:
			key=key+2295
			return key
		elif key==74:
			key=key+2259
			return key
		elif key==75:
			key=key+2251
			return key
		elif key==76:
			key=key+2279
			return key
		elif key==77:
			key=key+2229
			return key
		elif key==78 or key==119:
			key=key+2261
			return key
		elif key==80:
			key=key+2267
			return key
		elif key==81:
			key=key+2255
			return key
		elif key==82:
			key=key+2289
			return key
		elif key==85:
			key=key+2285
			return key
		elif key==86:
			key=key+2219
			return key
		elif key==88 or key==98:
			key=key+2250
			return key
		elif key==90:
			key=key+2225
			return key
		elif key==91:
			key=key+2220
			return key
		elif key==92:
			key=key+2292
			return key
		elif key==93:
			key=key+2226
			return key
		elif key==99:
			key=key+2232
			return key
		elif key==100:
			key=key+2242
			return key
		elif key==101:
			key=key+2274
			return key
		elif key==102:
			key=key+2211
			return key
		elif key==103 or key==116:
			key=key+2224
			return key
		elif key==105:
			key=key+2262
			return key
		elif key==106:
			key=key+2226
			return key
		elif key==107:
			key=key+2218
			return key
		elif key==108:
			key=key+2246
			return key
		elif key==109:
			key=key+2241
			return key
		elif key==110 or key==112:
			key=key+2234
			return key
		elif key==111:
			key=key+2268
			return key
		elif key==113:
			key=key+2222
			return key
		elif key==114 or key==126:
			key=key+2238
			return key
		elif key==117:
			key=key+2252
			return key
		elif key==118:
			key=key+2239
			return key
		elif key==120:
			key=key+2217
			return key
		elif key==121:
			key=key+2230
			return key
		elif key==123:
			key=key+2189
			return key
		elif key==124:
			key=key+2183
			return key		
		elif key==125:
			key=key+2195
			return key
		else:
			return key		
keys=Keyboard()								
def main():
	print "Not Allowed"

if __name__ == '__main__': main()
