import pandas as pd
import os.path
import csv

class ImgException(Exception):
    def __init__(self, msg='No msg'):
        self.msg = msg
def IDconvertor(Clothing_Genome_Project):
    if(os.path.isfile(Clothing_Genome_Project) == False):
        raise ImgException(Clothing_Genome_Project + ' not found')
    CGP = pd.read_excel(Clothing_Genome_Project)
    sizeColumn=7
    sizes={}
    index=1
    for row in range(1,CGP.shape[0]):
        size=CGP.iat[row,sizeColumn]
        if size not in sizes:
            sizes[size]=index
            index+=1
        CGP.iat[row,sizeColumn] = sizes[size]
    
    
    i=0 #process headers
    while i<len(CGP.columns.values):
        if "Unnamed" in CGP.columns.values[i]:
            CGP.columns.values[i] = ''
        i+=1
    CGP.to_excel('../test.xlsx',index=False)           
    with open('brandRules.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in sizes.items():
            writer.writerow([key, value])
IDconvertor("../test.xlsx")