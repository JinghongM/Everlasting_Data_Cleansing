import pandas as pd
import csv
CGP = pd.read_excel("test.xlsx")
speciescolumn=5
genuscolumn=4
species_error={}
#Leaveit=[1434, 1435, 1436, 1437, 1438, 1439, 1440,1032, 1033, 1034, 1035,1120, 1121,144,131, 132, 133, 134, 288, 424, 1366, 1367, 1368,506, 507, 508, 509, 510, 511, 512, 513,578,787,808, 809, 810, 811, 812, 813,815, 816, 830, 831, 832, 833, 834, 835, 903,974,975,1272,1441, 1442, 1443, 1444, 1445, 1446,1449, 1450,1691,1702,1703,131, 132, 133, 134, 288, 424, 1366, 1367, 1368,506, 507, 508, 509, 510, 511, 512, 513,578,787,808, 809, 810, 811, 812, 813,815, 816, 830, 831, 832, 833, 834, 835, 903,974,975,1272,1441, 1442, 1443, 1444, 1445, 1446,1449, 1450,1691,1702,1703]
for row in range(1,CGP.shape[0]):
	#if row in Leaveit:
#		continue
	species = str(CGP.iat[row, speciescolumn])
	if not species.isdigit() and species != "nan":
		if species in species_error:
			species_error[species].append(row)
		else:
			species_error[species]=[]
			species_error[species].append(row)
with open('species error.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in species_error.items():
       writer.writerow([key, value])