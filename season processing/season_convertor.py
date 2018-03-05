import pandas as pd
import copy
import os.path
class ImgException(Exception):
    def __init__(self, msg='No msg'):
        self.msg = msg
def seasonconvertor(Clothing_Genome_Project):
    if(os.path.isfile(Clothing_Genome_Project) == False):
        raise ImgException(Clothing_Genome_Project + ' not found')

    
    CGP = pd.read_excel(Clothing_Genome_Project)
    season={"Summer":1,"Spring":2,"Fall":3,"Winter":4}
    seasonColumnStart=14
    seasonColumnEnd=18

    seasoncolumnindex=[]
    for i in range(4):
    	seasoncolumnindex.append(season[CGP.iat[0,seasonColumnStart+i]])
    for row in range(1,CGP.shape[0]):
        print(row)
        Season = []
        for column in range(len(season)):
            if CGP.iat[row,column+seasonColumnStart] == 'x':
                Season.append(seasoncolumnindex[column])

        if len(Season) == 0:
            CGP.iat[row,seasonColumnStart] = 0
        elif len(Season) == 1:
            CGP.iat[row,seasonColumnStart] = Season[0]
        else:
            CGP.iat[row,seasonColumnStart] = Season[0]
            originRow=copy.deepcopy(CGP.iloc[row])
            for seasonID in Season[1:]:
                newrow = copy.deepcopy(originRow)
                newrow.iat[seasonColumnStart] = seasonID
                CGP = CGP.append(newrow)
    CGP = CGP.drop(CGP.columns[seasonColumnStart+1:seasonColumnEnd],axis = 1)
    i=0 #process headers
    while i<len(CGP.columns.values):
        if "Unnamed" in CGP.columns.values[i]:
            CGP.columns.values[i] = ''
        i+=1
    CGP.to_excel('test.xlsx',index=False)     
seasonconvertor('../test.xlsx')