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
from wx.grid import Grid
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
		wPanel.SetFont(font)
		wPanel.SetBackgroundColour('white')
		value=self.entry.GetValue()
		u=value.encode("utf-8")
		if value == "" or value == None:
			self.search.Disable()			
			style=wx.FRAME_TOOL_WINDOW
			mysize=(110,20)
			self.alert=MyFrame(parent=self.MainPanel,title="सावधान",size=mysize,style=style)
			notice=wx.StaticText(parent=self.alert,id=-1,label='कृपया शब्द लेख्नुहोस् । ',pos=(0,25))
			self.alert.Show()
			self.alert.Bind(wx.EVT_ENTER_WINDOW,self.OnEnter)
		else:
			try:
				result = mydb.select(u)
				if u == result['शब्द']:
					fl = mydb.get_field_length(u)
					word = wx.StaticBox(wPanel,label=u)
					result.pop('शब्द')
					stboxsizer=wx.StaticBoxSizer(word,orient=wx.VERTICAL)
					word_grid = Grid(wPanel)
					word_grid.SetSize((430, 220))
					word_grid.CreateGrid(fl-1, 2)
					word_grid.SetRowLabelSize(0)
					word_grid.SetCellHighlightPenWidth(0)
					word_grid.EnableEditing(False)
					word_grid.SetColLabelSize(0)
					vbox = wx.BoxSizer(wx.VERTICAL|wx.SHAPED)
					i = 0
					for k, v in result.items():
						word_grid.SetCellRenderer(i, 0, wx.grid.GridCellAutoWrapStringRenderer())
						word_grid.SetCellValue(i, 0, k)
						word_grid.AutoSizeColumn(0)
						# wraps text inside a cell
						word_grid.SetCellRenderer(i, 1, wx.grid.GridCellAutoWrapStringRenderer())
						word_grid.SetCellValue(i, 1, v)
						word_grid.AutoSizeColumn(1)
						word_grid.AutoSizeRows(i)
						i += 1
					vbox.Add(word_grid, wx.EXPAND)
					stboxsizer.Add(vbox,wx.SHAPED)
					wPanel.SetSizer(stboxsizer,wx.EXPAND)
				else:
					style=wx.FRAME_TOOL_WINDOW
					mysize=(150,30)
					self.alert=MyFrame(parent=self.MainPanel,title="सावधान",size=mysize,style=style)
					notice=wx.StaticText(parent=self.alert,id=-1,label='माफ गर्नुहोस, खोजिएको शब्द यहाँ छैन ।',pos=(0,25))
					self.alert.Show()
					self.alert.Bind(wx.EVT_ENTER_WINDOW,self.OnEnter)
			except:
				style=wx.FRAME_TOOL_WINDOW
				mysize=(200,30)
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
