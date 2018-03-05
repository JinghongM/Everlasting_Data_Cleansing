import pandas as pd
import copy
import os.path
Pattern=6
Material=7
Speciescolumn=4
Genuscolumn=3
CGP = pd.read_excel("../Realdata.xlsx")
for row in range(0,CGP.shape[0]):
	Species = str(CGP.iat[row,Speciescolumn])
	if "Longsleeve Peter Pan Collar" == Species:
		print(row)
		CGP.iat[row,Genuscolumn] = "Blouse"
		CGP.iat[row,Speciescolumn] = "Long Sleeve"
		newRow=copy.deepcopy(CGP.loc[row])
		newRow.iat[Speciescolumn] = "Peter Pan Collar"
		CGP=CGP.append(newRow1) 
		
i=0 #process headers
while i<len(CGP.columns.values):
	if "Unnamed" in CGP.columns.values[i]:
		CGP.columns.values[i] = ''
	i+=1
CGP.to_excel('../Realdata.xlsx',index=False) 