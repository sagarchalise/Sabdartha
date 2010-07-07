#!/usr/bin/env python
import os,sys
p=os.getcwd()
mypath= p+'/Database'
sys.path.append(mypath)
from PyDbLite import Base

class DataBase():
	def __init__(self):
		self.db=Base(mypath+'/data.pdl')
		self.db.open()
		
	def select(self,value):
		self.value=value
		res = [r for r in self.db if r['words'] == self.value]
		for v in res:
			val=[z for k,z in v.items()]
			key=[k for k,z in v.items()]
			result = dict(zip(key, val))
			return result
				
mydb=DataBase()
