#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       action.py
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
import re
from data import mydb
from myFrame import *
from keyboard import *

class Words():
	def __init__(self,parent):
		self.parent=parent
		self.entry=wx.TextCtrl(parent=parent,pos=(75,55),size=(250,30))
		self.outlines()
		temp=decor.getImage('search.png')		
		self.search=buttons.GenBitmapButton(parent=self.parent,bitmap=temp,pos=(338,53.5),size=(65,30),style=0)
		self.MainPanel=wx.Panel(parent=self.parent,pos=(3,95),size=(443,230))
		temp=decor.getImage(imageFile='splash.sbd')
		bmp = wx.StaticBitmap(parent=self.MainPanel, bitmap=temp)		
		self.entry.Bind(wx.EVT_CHAR,self.getKeys)
		self.search.Bind(wx.EVT_BUTTON,self.showDatas)

	def getKeys(self,event):
		k=event.GetKeyCode()		
		if k==8 or k==314 or k==315 or k==316 or k==317 or k==306 or k==311 or k==308:
			event.Skip(True)
		else:
			mykey=keys.GetNepKey(k)
			event.SetUnicodeKey(mykey)
			self.entry.EmulateKeyPress(event)
	
	def showDatas(self,event):
		self.MainPanel.Hide()		
		font=decor.getFonts(size=12.5,weight=wx.FONTWEIGHT_NORMAL)
		wPanel=wx.Panel(parent=self.parent,pos=(3,95),size=(443,230))
		vbox1=wx.BoxSizer(wx.VERTICAL)
		wPanel.SetFont(font)
		wPanel.SetBackgroundColour('white')
		value=self.entry.GetValue()
		u=value.encode("utf-8")
		if value=="":
			self.search.Disable()			
			style=wx.FRAME_TOOL_WINDOW
			mysize=(110,20)
			self.alert=MyFrame(parent=self.MainPanel,title="सावधान",size=mysize,style=style)
			notice=wx.StaticText(parent=self.alert,id=-1,label='कृपया शब्द लेख्नुहोस् । ',pos=(0,25))
			self.alert.Show()
			self.alert.Bind(wx.EVT_ENTER_WINDOW,self.OnEnter)
		else:
			result=mydb.select(u)
			if u==result.Words:
				scroll=wx.Panel(wPanel)
				word=wx.StaticBox(scroll,label=result.Words)
				stboxsizer=wx.StaticBoxSizer(word,orient=wx.VERTICAL)
				vbox=wx.BoxSizer(wx.VERTICAL|wx.SHAPED)
				grid=wx.GridSizer(5,1,10,5)
				grid.Add(wx.StaticText(scroll,label= 'पदवर्ग: '),wx.ALIGN_CENTER)
				grid.Add(wx.StaticText(scroll,label=result.Speech))
				grid.Add(wx.StaticText(scroll,label='अर्थ: '),wx.ALIGN_CENTER)
				grid.Add(wx.StaticText(scroll,label=result.Meaning))
				if result.Synonym == None:
					grid.Add(wx.StaticText(scroll,label='विपरितार्थक: '),wx.ALIGN_CENTER)
					grid.Add(wx.StaticText(scroll,label=result.Antonym))
					grid.Add(wx.StaticText(scroll,label='अङ्ग्रेजी: '),wx.ALIGN_CENTER)
					grid.Add(wx.StaticText(scroll,label=result.English))				
				elif result.Antonym == None:
					grid.Add(wx.StaticText(scroll,label= 'पर्यायवाचक: '),wx.ALIGN_CENTER)
					grid.Add(wx.StaticText(scroll,label=result.Synonym))
					grid.Add(wx.StaticText(scroll,label='अङ्ग्रेजी: '),wx.ALIGN_CENTER)
					grid.Add(wx.StaticText(scroll,label=result.English))
				else:
					grid.Add(wx.StaticText(scroll,label='विपरितार्थक :'),wx.ALIGN_CENTER)
					grid.Add(wx.StaticText(scroll,label=result.Synonym))
					grid.Add(wx.StaticText(scroll,label='पर्यायवाचक :'),wx.ALIGN_CENTER)
					grid.Add(wx.StaticText(scroll,label=result.Antonym))
					grid.Add(wx.StaticText(scroll,label='अङ्ग्रेजी: ' ),wx.ALIGN_CENTER)
					grid.Add(wx.StaticText(scroll,label=result.English))
				vbox.Add(grid)
				stboxsizer.Add(vbox,wx.SHAPED)
				scroll.SetSizer(stboxsizer)
				vbox1.Add(scroll,wx.SHAPED)
				wPanel.SetSizer(vbox1,wx.EXPAND)
			elif u!=result.Words:
				style=wx.FRAME_TOOL_WINDOW
				mysize=(110,20)
				self.alert=MyFrame(parent=self.MainPanel,title="सावधान",size=mysize,style=style)
				notice=wx.StaticText(parent=self.alert,id=-1,label='माफ गर्नुहोस, खोजिएको शब्द यहाँ छैन ।',pos=(0,25))
				self.alert.Show()
				self.alert.Bind(wx.EVT_ENTER_WINDOW,self.OnEnter)					
		self.entry.Clear()		

	def outlines(self):
		font=decor.getFonts(size=11,weight=wx.FONTWEIGHT_NORMAL,family=wx.FONTFAMILY_SWISS)
		self.entry.SetFont(font)
		self.entry.SetMaxLength(25)
		self.entry.SetFocus()
		self.entry.CanCopy()
		self.entry.CanCut()
		self.entry.CanPaste()
		self.entry.CanUndo()
		self.entry.CanRedo()
		self.entry.SetValue('खोज्ने शब्द यहा लेख्नुहोस् ।  ')
	
	def OnEnter(self,event):
		self.search.Enable()
		self.alert.Close()	
	
def main():
	print "Hello, Not allowed"
	

if __name__ == '__main__': main()
