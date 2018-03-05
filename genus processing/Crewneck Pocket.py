import pandas as pd
import copy
import os.path
Pattern=6
Material=7
Species=4
CGP = pd.read_excel("../Realdata.xlsx")
for row in range(1,CGP.shape[0]):
	genus = str(CGP.iat[row,3])
	if "Crewneck Pocket" == genus:
		print(row)
		CGP.iat[row,3] = "TShirt"
		CGP.iat[row,Species] ="Crew Neck"
		originRow = copy.deepcopy(CGP.loc[row])
		newRow = copy.deepcopy(originRow)
		newRow.iat[Species]="Pocket"
		CGP=CGP.append(newRow) 

i=0 #process headers
while i<len(CGP.columns.values):
	if "Unnamed" in CGP.columns.values[i]:
		CGP.columns.values[i] = ''
	i+=1
CGP.to_excel('../Realdata.xlsx',index=False) 