#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
mypath= os.path.join(os.path.dirname(os.path.abspath(__file__)),'database')
from buzhug import Base

class DataBase():
    def __init__(self):
        self.db=Base(mypath)
        self.sfield = {'शब्द': 'Words', 
                        'पद': 'Speech', 
                        'अर्थ': 'Meaning', 
                        'पर्यायवाचि': 'Synonym', 
                        'विपरीतार्थक': 'Antonym', 
                        'अंग्रेजी': 'English'}
        self.db.open()
            	
    def _get_attribute(self,args):
        ret_val = {}
        for k,f in self.sfield.items():
            ret_val[k] = getattr(args, f)
            if ret_val[k] == None:
                ret_val.pop(k)
        return ret_val
    def select(self,value):
        self.record = self.db.select([f for f in self.sfield.itervalues()],Words=value)
        for v in self.record:
            self.g = self._get_attribute(v)
            return self.g             
        self.db.close()             
    
    def fields(self):
        print self.db.field_names                   		
	
    def get_field_length(self):
        return len(self.g)

mydb=DataBase()
if __name__=='__main__':print "Hello, Not Allowed."

