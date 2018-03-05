import pandas as pd
import copy
import os.path
CGP = pd.read_excel("../Realdata.xlsx")
for row in range(1,CGP.shape[0]):
	genus = str(CGP.iat[row,3])
	if "Cashmere" in genus:
		print(row)
		CGP.iat[row,3] = genus.replace("Cashmere ","")
		CGP.iat[row,7] = "Cashmere"
    
i=0 #process headers
while i<len(CGP.columns.values):
	if "Unnamed" in CGP.columns.values[i]:
		CGP.columns.values[i] = ''
	i+=1
CGP.to_excel('../Realdata.xlsx',index=False) 