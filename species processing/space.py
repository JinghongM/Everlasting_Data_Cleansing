import pandas as pd
import copy
import os.path
Pattern=6
Material=7
speciescolumn=4
genuscolumn=3
CGP = pd.read_excel("../Realdata.xlsx")
for row in range(1,CGP.shape[0]):
	species = str(CGP.iat[row,speciescolumn])
	genus = str(CGP.iat[row,genuscolumn])

	if " " == species:
		print(row)
		CGP.iat[row,speciescolumn] = ""
	if " " == genus:
		print(row)
		CGP.iat[row,genuscolumn] = ""

    
i=0 #process headers
while i<len(CGP.columns.values):
	if "Unnamed" in CGP.columns.values[i]:
		CGP.columns.values[i] = ''
	i+=1
CGP.to_excel('../Realdata.xlsx',index=False) 