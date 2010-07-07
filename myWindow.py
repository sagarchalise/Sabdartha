#!/usr/bin/env python
# -*- coding: utf-8 -*-
#       myWindow.py
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
from myFrame import *
from action import *

helpstyle=wx.FRAME_TOOL_WINDOW |wx.SYSTEM_MENU
helptitle='शब्दार्थ मद्दत '
class MyWindow():
	def __init__(self,myparent):
		self.parent=myparent
		temp=decor.getImage(imageFile='Mainwindow.png')
		self.panel = wx.Panel(self.parent, -1)
		self.bmp = wx.StaticBitmap(parent=self.panel, bitmap=temp)
		self.menuPanel=wx.Panel(parent=self.panel,pos=(5,30),size=(440,20))
		cross=decor.getImage('cross.png')
		self.close=buttons.GenBitmapButton(parent=self.panel,bitmap=cross,pos=(418.5,5.5),size=(18,15))
		minus=decor.getImage('minus.png')
		self.mini=buttons.GenBitmapButton(parent=self.panel,bitmap=minus,pos=(388,5.5),size=(21,14))
		self.help=wx.Button(self.menuPanel,label='मद्दत',style=wx.NO_BORDER)
		self.index=wx.Button(self.menuPanel,label='अनुसुचि',style=wx.NO_BORDER)
		self.about=wx.Button(self.menuPanel,label='शब्दार्थ बारेमा',style=wx.NO_BORDER)
		self.main=Words(parent=self.panel)
		self.myLayouts()
		
	def myLayouts(self):
		box=wx.BoxSizer(wx.HORIZONTAL)
		box.Add(self.help,1, wx.EXPAND |  wx.ALL,-3)
		box.Add(self.index,1, wx.EXPAND |  wx.ALL,-5)
		box.Add(self.about,1, wx.EXPAND |  wx.ALL,-3)
		self.menuPanel.SetSizer(box)
		self.myEvents()
	
	def myEvents(self):
		self.close.Bind(wx.EVT_BUTTON,self.OnClick)
		self.mini.Bind(wx.EVT_ICONIZE,self.OnMinimize)
		self.about.Bind(wx.EVT_BUTTON,self.OnAbout)
		self.help.Bind(wx.EVT_BUTTON,self.OnHelp)
		self.index.Bind(wx.EVT_BUTTON,self.OnIndex)
		
	def OnAbout(self,event):
		self.about.Disable()
		w=f.readfile("we.txt")
		lic=f.readfile("licence.txt")
		self.info =MyFrame(parent=self.menuPanel,title=helptitle,size=(300,300),style=helpstyle)
		showhelp=wx.StaticBox(self.info,label="शब्दार्थ बारेमा ",pos=(1,1),size=(299,298))
		inPanel=wx.Panel(self.info,pos=(2,18),size=(298,280),style=wx.SUNKEN_BORDER)
		mysize=decor.getSize(imageFile='ola.png')
		temp=decor.getImage(imageFile='ola.png')
		ico=wx.StaticBitmap(inPanel,bitmap=temp,size=mysize,pos=(100,5))
		line=wx.StaticLine(inPanel,pos=(0,145),size=(300,2),style=wx.LI_HORIZONTAL)
		copy=wx.StaticText(inPanel,label="सर्वाधिकार शब्दार्थ समुह",pos=(75,150),style=wx.ALIGN_CENTER)
		line2=wx.StaticLine(inPanel,pos=(0,170),size=(300,2),style=wx.LI_HORIZONTAL)
		licence=wx.StaticText(inPanel,label=lic,pos=(8,35))
		we=wx.StaticText(inPanel,label=w,pos=(5,180))
		url=wx.HyperlinkCtrl(parent=inPanel,id=-1,label="GNU GPL",url="http://www.gnu.org/licenses/gpl.html",pos=(90,96))
		self.huncha=buttons.GenButton(inPanel,label='हुन्छ ',pos=(100,240),style=wx.RAISED_BORDER)
		self.huncha.Bind(wx.EVT_BUTTON,self.onClick)
		self.info.Show()		
	
	def OnHelp(self,event):
		self.help.Disable()
		w=f.readfile('words.txt')
		k=f.readfile("keys.txt")
		t=f.readfile("type.txt")
		self.info =MyFrame(parent=self.menuPanel,title=helptitle,size=(600,500),style=helpstyle)
		vbox=wx.BoxSizer(wx.HORIZONTAL)
		help=wx.StaticText(self.info,label="मद्दत ",pos=(275,0))
		inPanel=wx.Panel(self.info,pos=(15,20),size=(565,210),style=wx.SUNKEN_BORDER)
		showhelp=wx.StaticBox(inPanel,label="टाइप उदाहरण ",pos=(1,1),size=(568,195))
		copy=wx.StaticText(inPanel,label="जोड चिन्ह सुचक हो (+) टाइप नगर्नु होला ।",pos=(125,15))
		wordBox=wx.StaticBox(inPanel,label="शब्द ",pos=(2,30),size=(100,150))
		typeBox=wx.StaticBox(inPanel,label="बनोट ",pos=(105,30),size=(250,150))
		words=wx.StaticText(inPanel,label=w,pos=(10,45))
		keyBox=wx.StaticBox(inPanel,label="टाइप गर्ने किहरु ",pos=(355,30),size=(210,125))
		type=wx.StaticText(inPanel,label=t,pos=(110,45))
		keys=wx.StaticText(inPanel,label=k,pos=(360,50))
		font=decor.getFonts(size=12,weight=wx.FONTWEIGHT_NORMAL)
		help.SetFont(font)
		imge="keyboard.sbd"
		size=decor.getSize(imge)
		imgPanel=wx.Panel(parent=self.info,pos=(0,215),size=size,style=wx.BORDER_SUNKEN)
		img=decor.getImage(imge)
		keyboard=wx.StaticBitmap(imgPanel,bitmap=img,pos=(-15,-15))
		huncha=buttons.GenButton(inPanel,label='हुन्छ ',pos=(475,160),style=wx.RAISED_BORDER)
		self.info.Show()
		huncha.Bind(wx.EVT_BUTTON,self.onClick)
			
	def OnIndex(self,event):
		self.index.Disable()
		lic=f.readfile("index.txt")
		self.info =MyFrame(parent=self.menuPanel,title=helptitle,size=(400,325),style=helpstyle)
		showhelp=wx.StaticBox(self.info,label="अनुसुचि ",pos=(1,1),size=(399,324))
		inPanel=wx.Panel(self.info,pos=(3,18),size=(395,305),style=wx.SUNKEN_BORDER)
		index=wx.StaticText(inPanel,label=lic,pos=(2,3))
		huncha=buttons.GenButton(inPanel,label='हुन्छ ',pos=(300,270),style=wx.RAISED_BORDER)
		self.info.Show()
		huncha.Bind(wx.EVT_BUTTON,self.onClick)
					
	def OnClick(self,event):
		self.parent.Disable()
		size=(40,30)
		temp=decor.getImage('error.png')
		self.info=MyFrame(parent=self.panel,title="सुचना ",size=(200,75),style=wx.FRAME_TOOL_WINDOW)
		pnl=wx.Panel(self.info,style=wx.SUNKEN_BORDER)
		self.bmp=wx.StaticBitmap(pnl,bitmap=temp,pos=(10,15),size=(48,48))
		query=wx.StaticText(pnl,label="के तपाई बन्द गर्न चाहनुहुन्छ ? " ,pos=(30,15))
		self.yes=buttons.GenButton(pnl,label="हुन्छ ", pos=(20,40),size=size,style=wx.RAISED_BORDER)
		self.no=buttons.GenButton(pnl,label="होइन ",pos=(75,40),size=size,style=wx.RAISED_BORDER)
		self.yes.Bind(wx.EVT_BUTTON,self.CloseWindow)
		self.no.Bind(wx.EVT_BUTTON,self.onClick)
		self.info.Show()
		self.info.Centre()
					
	def onClick(self,event):
		self.help.Enable()
		self.about.Enable()
		self.parent.Enable()
		self.index.Enable()
		self.info.Close()
	
	def OnMinimize(self,event):
		self.parent.Iconized()

	def CloseWindow(self,event):
		self.info.Destroy()
		self.parent.Destroy()
								
def main():
	print "Not Allowed"
if __name__ == '__main__': main()
