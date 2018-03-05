import pandas as pd
import copy
import os.path
CGP = pd.read_excel("../Realdata.xlsx")

for row in range(0,CGP.shape[0]):
	if CGP.iat[row,3] == "Classic":
		print(row)
		CGP.iat[row,3] ="Overalls"
    
i=0 #process headers
while i<len(CGP.columns.values):
	if "Unnamed" in CGP.columns.values[i]:
		CGP.columns.values[i] = ''
	i+=1
CGP.to_excel('../Realdata.xlsx',index=False) 