import pandas as pd
import copy
import os.path
Patterncolumn=6
Material=7
speciescolumn=4
CGP = pd.read_excel("../Realdata.xlsx")
for row in range(1,CGP.shape[0]):
	species = str(CGP.iat[row,speciescolumn])
	if "Terry Cloth" in species:
		print(row)
		CGP.iat[row,speciescolumn] = species.replace("Terry Cloth","")
		CGP.iat[row,Material] = "Terry"
    
i=0 #process headers
while i<len(CGP.columns.values):
	if "Unnamed" in CGP.columns.values[i]:
		CGP.columns.values[i] = ''
	i+=1
CGP.to_excel('../Realdata.xlsx',index=False) 