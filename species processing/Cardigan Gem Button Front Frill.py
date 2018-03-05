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
	if "Cardigan Gem Button Front Frill" in Species:
		CGP.iat[row,Genuscolumn] = "Sweater"
		CGP.iat[row,Speciescolumn] = "Cardigan"
		originRow=copy.deepcopy(CGP.loc[row])
		print(row)
		newRow = copy.deepcopy(originRow)
		newRow.iat[Speciescolumn]="w/ Bloomers"
		CGP=CGP.append(newRow) 
    
i=0 #process headers
while i<len(CGP.columns.values):
	if "Unnamed" in CGP.columns.values[i]:
		CGP.columns.values[i] = ''
	i+=1
CGP.to_excel('../Realdata.xlsx',index=False) 