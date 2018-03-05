import numpy as np
import pandas as pd
CGP = pd.read_excel("../Realdata.xlsx",index=False)
Leaveit=[963,1060,1394,176,963,868, 869, 870, 871,911, 912,951, 952,819,176,1434, 1435, 1436, 1437, 1438, 1439, 1440,1032, 1033, 1034, 1035,1120, 1121,144,131, 132, 133, 134, 288, 424, 1366, 1367, 1368,506, 507, 508, 509, 510, 511, 512, 513,578,787,808, 809, 810, 811, 812, 813,815, 816, 830, 831, 832, 833, 834, 835, 903,974,975,1272,1441, 1442, 1443, 1444, 1445, 1446,1449, 1450,1691,1702,1703,131, 132, 133, 134, 288, 424, 1366, 1367, 1368,506, 507, 508, 509, 510, 511, 512, 513,578,787,808, 809, 810, 811, 812, 813,815, 816, 830, 831, 832, 833, 834, 835, 903,974,975,1272,1441, 1442, 1443, 1444, 1445, 1446,1449, 1450,1691,1702,1703]
Leaveit = sorted(list(set(Leaveit)))[::-1]
uselessrows=[]
for uselessrow in Leaveit:
 	print(uselessrow)
 	uselessrows.append(CGP.loc[uselessrow])

df = pd.DataFrame(uselessrows)
CGP = CGP.drop(CGP.index[Leaveit])
df.to_excel("uselessgenus.xlsx",index=False)
CGP.to_excel('../Realdata.xlsx',index=False)
