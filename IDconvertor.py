# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:35:27 2017

@author: Jinghong Miao
"""
import pandas as pd
import copy
import os.path
from fuzzywuzzy import fuzz
class ImgException(Exception):
    def __init__(self, msg='No msg'):
        self.msg = msg
def IDconvertor(Clothing_Genome_Project,Item_ID_Info):
    if(os.path.isfile(Clothing_Genome_Project) == False):
        raise ImgException(Clothing_Genome_Project + ' not found')
    if(os.path.isfile(Item_ID_Info) == False):
        raise ImgException(Item_ID_Info + ' not found')
    def findIDs(SearchWords,Dictionaries):
        if SearchWords == None:
            return -1,-1
        maxRatio=0
        maxStyleID=""
        maxSubValue=""
        for StyleID,subDictionary in Dictionaries.items():
            for subKey,subValue in subDictionary.items():
                if fuzz.ratio(str(SearchWords),subKey)>maxRatio:
                    maxRatio = fuzz.ratio(SearchWords,subKey)
                    maxSubValue=subValue
                    maxStyleID=StyleID

        if(maxRatio<50):
            return -1,-1
        else:

            return maxStyleID,maxSubValue
    def splitGenus(Genus,Style_Genus):#input a genus with an empty species,return a genusID and the correct species
        for style, subDictionary in Style_Genus.items():
            for genus,genusID in subDictionary.items():
                if(genus in Genus):
                    print(Genus)
                    return style,genusID,Genus.replace(genus,"")
        return -1,-1,-1
                    

    Quantity=9 #main table column
    EWNumber = 0 #main table column
    GenusColumn=3 #main table column
    SpeciesColumn=4 #main table column
    GenreColumnStart = 12 #Main table column
    GenreColumnEnd = 18 #Main table column
    StyleGenreIDStartColumn = 6 #ID table column
    StyleGenreIDENDColumn = 9 #ID table column
    StyleSpeciesIDStartColumn = 10 #ID table column
    StyleSpeciesIDEndColumn = 13 #ID table column
    
    IInfo = pd.read_excel(Item_ID_Info)
    CGP = pd.read_excel(Clothing_Genome_Project)
    CGP.insert(3,'Style',None)
    StyleColumn = 3
    Quantity +=1
    GenusColumn += 1
    SpeciesColumn += 1
    GenreColumnStart += 1
    GenreColumnEnd += 1

    #process Style,Genus and Species
    Style_Genus = {} # this is a dictionary which key is Stype Genre Genus ID, value is the Special ID
    Genres = {}
    Style_Species = {}
    for column in range(StyleGenreIDStartColumn,StyleGenreIDENDColumn+1): #store Genus ID into Genus_Species dictionary and create a entry
                                                                       #which is general genus name
        GenusBlock = IInfo.iat[0,column]
        StyleName = GenusBlock[:GenusBlock.find("=")]
        StyleID = int(GenusBlock[GenusBlock.find("=")+1:])
        Style_Genus[StyleID] = {}
        Style_Genus[StyleID][StyleName] = StyleID
        
    for column in range(StyleSpeciesIDStartColumn,StyleSpeciesIDEndColumn+1): #store Genus ID into Genus_Species dictionary and create a entry
                                                         #which is general genus name
        SpeciesBlock = IInfo.iat[0,column]
        StyleName = SpeciesBlock[:SpeciesBlock.find("=")]
        StyleID = int(SpeciesBlock[SpeciesBlock.find("=")+1:])
        Style_Species[StyleID] = {}
        Style_Species[StyleID][StyleName] = StyleID
        
    for column in Style_Genus.keys(): #store all specific genus into Style_Genus and Style_Species
        for row in range(1,IInfo.shape[0]):
            if str(IInfo.iat[row,StyleGenreIDStartColumn+column]) =='nan':
                break
            else:
                Block = IInfo.iat[row,StyleGenreIDStartColumn+column]
                GenusName = Block[:Block.find("=")]
                GenusID = Block[Block.find("=") + 1:]
                Style_Genus[column][GenusName] = GenusID
        for row in range(1, IInfo.shape[0]):
            if str(IInfo.iat[row,StyleSpeciesIDStartColumn+column]) == 'nan':
                break
            else:
                Block = IInfo.iat[row,StyleSpeciesIDStartColumn+column]
                SpeciesName = Block[:Block.find("=")]
                SpeciesID = Block[Block.find("=") + 1:]
                Style_Species[column][SpeciesName] = SpeciesID
    # for row in range(1,CGP.shape[0]):#preprocessing empty species entities
    #     Species = CGP.iat[row,SpeciesColumn]
    #     Genus = CGP.iat[row,GenusColumn]

    #     if str(Species)=="nan" and str(Genus) == "nan":
    #         continue
    #     else: #separate all genus and species words and store into a SearchKeyWords list
    #         if str(Species) == 'nan':
    #             styleID,genusID,species = splitGenus(Genus,Style_Genus)
    #             if(genusID!=-1 and species != -1 and styleID != -1):
    #                 CGP.iat[row,SpeciesColumn] = species
    #                 CGP.iat[row,GenusColumn] = genusID
    #                 CGP.iat[row,StyleColumn] = styleID
    # return

    for row in range(1,CGP.shape[0]):

        Species = CGP.iat[row,SpeciesColumn]
        Genus = CGP.iat[row,GenusColumn]

        #SearchKeyWords_Genus=[]
        #SearchKeyWords_Species=[]
        if str(Species)=="nan" and str(Genus) == "nan":
            print("No Genus and Species at " + str(row))
            continue

        else:
            StyleID01, GenusID = findIDs(str(Genus),Style_Genus)
            StyleID02, SpeciesID = findIDs(str(Species),Style_Species)

            if StyleID01 == -1 and StyleID02 == -1:
                print("Can't find Style at" + str(row))
                CGP.iat[row,StyleColumn]="Not Found"
                continue
            else:
                if StyleID01 == StyleID02:
                    CGP.iat[row,StyleColumn] = StyleID01
                    CGP.iat[row,GenusColumn] = GenusID
                    CGP.iat[row,SpeciesColumn] = SpeciesID
                    continue
                elif StyleID01 != -1:
                    CGP.iat[row, StyleColumn] = StyleID01
                    CGP.iat[row,GenusColumn] = GenusID
                    if SpeciesID != -1:
                        CGP.iat[row,SpeciesColumn] = SpeciesID
                    continue
                elif StyleID02 == -1:
                    CGP.iat[row, StyleColumn] = StyleID02
                    CGP.iat[row,SpeciesColumn] = SpeciesID
            
            # elif type(Genus) == int or Genus.isdigit():
            #     print("...")
            #     StyleID02, SpeciesID = findIDs(str(Species),Style_Species)
            #     CGP.iat[row,SpeciesColumn]=SpeciesID
            
    #process quantity
    for row in range(1,CGP.shape[0]):
        originRow=copy.deepcopy(CGP.loc[row])
        quantity = str(originRow.iat[Quantity]) 
        CGP.iat[row,EWNumber] = str(originRow.iat[EWNumber]) + '-1'
        
        if quantity !='nan' and quantity != '1':
            for i in range(2,int(quantity)+1):
                newrow = copy.deepcopy(originRow)
                newrow.iat[EWNumber] = str(originRow.iat[EWNumber]) + '-'+ str(i)
                CGP=CGP.append(newrow) 
    #process genre
    for genre in IInfo['Genre']:
        if str(genre) == 'nan':
            break
        else:
            Genres[genre[:genre.find('=')]] = genre[genre.find('=')+1:]
    GenreTitle = []
    for i in range(GenreColumnStart,GenreColumnEnd):
        GenreTitle.append(CGP.iat[0,i])
    print(GenreTitle)
    for element in range(len(GenreTitle)):
        for char in GenreTitle[element].split('/'):
            if char in Genres:
                GenreTitle[element] = Genres[char]
    print(Genres)

    for row in range(1,CGP.shape[0]):
        genres = []
        for column in range(len(GenreTitle)):
            if CGP.iat[row,column+GenreColumnStart] == 'x':
                genres.append(GenreTitle[column])

        if len(genres) == 0:
            CGP.iat[row,GenreColumnStart] = 0
        elif len(genres) == 1:
            CGP.iat[row,GenreColumnStart] = genres[0]
        else:
            CGP.iat[row,GenreColumnStart] = genres[0]
            originRow=copy.deepcopy(CGP.iloc[row])
            for genreId in genres[1:]:
                newrow = copy.deepcopy(originRow)
                newrow.iat[GenreColumnStart] = genreId
                CGP = CGP.append(newrow)
    CGP = CGP.drop(CGP.columns[GenreColumnStart+1:GenreColumnEnd],axis = 1)
    CGP = CGP.drop(CGP.columns[Quantity],axis = 1)
    
    i=0 #process headers
    while i<len(CGP.columns.values):
        if "Unnamed" in CGP.columns.values[i]:
            CGP.columns.values[i] = ''
        i+=1
    CGP.to_excel('test.xlsx',index=False)          
IDconvertor('Realdata.xlsx','Item ID Info.xlsx')