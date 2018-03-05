import pandas as pd
CGP = pd.read_excel("speciesRules.xlsx")
CGP.insert(1,"species",None)
for row in range(CGP.shape[0]):
	record=CGP.iat[row,0]
	species=record[:record.find("=")]
	index=record[record.find("=")+1:]
	print(species)
	print(index)
	CGP.iat[row,0] = species
	CGP.iat[row,1] = index
CGP.to_csv('speciesRules.csv',index=False)          
