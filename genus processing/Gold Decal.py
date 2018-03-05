import pandas as pd
import copy
import os.path
Pattern=6
Material=7
Speciescolumn=4
Genuscolumn=3
CGP = pd.read_excel("../Realdata.xlsx")
for row in range(0,CGP.shape[0]):
	genus = str(CGP.iat[row,Genuscolumn])
	species = str(CGP.iat[row,Speciescolumn])
	if "Gold Decal" in genus:
		print(row)
		CGP.iat[row,Genuscolumn] = genus.replace(" Gold Decal", "")
		CGP.iat[row,Pattern] = "Gold Decal" 
	if "Gold Decal" in species:
		print(row)
		CGP.iat[row,Genuscolumn] = species.replace(" Gold Decal", "")
		CGP.iat[row,Pattern] = "Gold Decal"
i=0 #process headers
while i<len(CGP.columns.values):
	if "Unnamed" in CGP.columns.values[i]:
		CGP.columns.values[i] = ''
	i+=1
CGP.to_excel('../Realdata.xlsx',index=False) 