#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       library.py
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
try:
	import wx
	import wx.lib.buttons as buttons	
except ImportError:
	raise ImportError,"You need wxpython 2.8 to run this application"

myimagepath= 'images/'

class Decorations():
	imageFile=''
	def getImage(self,imageFile):
		image=myimagepath+imageFile
		self.img=wx.Image(image, wx.BITMAP_TYPE_ANY)
		self.temp=self.img.ConvertToBitmap()
		return self.temp
				
	def getSize(self,imageFile):
		self.temp=self.getImage(imageFile)
		self.size=self.temp.GetWidth(),self.temp.GetHeight()
		return self.size
	
	def getIcon(self,imageFile):
		image=myimagepath+imageFile
		icon = wx.Icon(image, wx.BITMAP_TYPE_ICO)
		return icon		

	def getSplash(self,imageFile):
		self.img = self.getImage(imageFile)
		splash=wx.SplashScreen(self.img,wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,1000,None)
		return splash
	
	def getFonts(self,size,weight,family=wx.FONTFAMILY_ROMAN):
		self.font=wx.Font(pointSize=size,family=family,weight=weight,style=wx.FONTSTYLE_NORMAL)
		return self.font

decor=Decorations()
if __name__=="__main__": print "Not Allowed"
