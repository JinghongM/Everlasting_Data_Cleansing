# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:52:26 2017

@author: Jinghong Miao
"""

import pandas as pd
import os.path
class ImgException(Exception):
    def __init__(self, msg='No msg'):
        self.msg = msg
columnsNotToDelete=[]
file_name=input("type filename to separate(excel only):")
if(os.path.isfile(file_name) == False):
        raise ImgException(file_name + ' not found')
    
destination_name=input("type filename to save(csv only):")
while(1):
    a=input("type columns to separate(type nothing to stop):")
    if(a == ""):
        break
    else:
        columnsNotToDelete.append(int(a))

raw_file = pd.read_excel(file_name)
columnNumber=raw_file.shape[1]
columnToDelete=list(set(list(range(columnNumber)))-set(columnsNotToDelete))
for column in sorted(columnToDelete)[::-1]:
    raw_file = raw_file.drop(raw_file.columns[column], axis=1)
raw_file.to_csv(destination_name,index=False,header=None)     
