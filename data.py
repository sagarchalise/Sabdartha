#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
mypath= os.path.join(os.path.dirname(os.path.abspath(__file__)),'database')
from buzhug import Base

class DataBase():
    def __init__(self):
        self.db=Base(mypath)
        self.db.open()
            	
    def select(self,value):
        record =self.db.select(['words','meaning'],words=value)
        for v in record:
            return v
     
    def fields(self):
        print self.db.field_names                   		
mydb=DataBase()

