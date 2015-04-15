'''
Created on 15 mars 2015

@author: Pierre.Parrend
'''
#from ai.normalize import Normalize
#from string import string
#from sets import set

import csv


class Normalizer():

    # NOT used
    def showDataset(self, dataFile):
        print("Show Dataset")
        data= open(irisFile,'r')
        for line in data:
            line = str.strip(line)
            print(line)
    
    def show_matrix_dataset(self, iris_data_matrix):
        print("Show matrix dataset")
        for row in iris_data_matrix:
            print(row)
    
    def load_csv(self, dataFile):
        # print("Load CSV from "+dataFile)
        
        data_matrix = []
         
        data = open(dataFile,'r')
        reader = csv.reader(data)
        firstLine = True
        rowLength=0
        for row in reader:
            #print(row)
            if firstLine:#remove column names
                firstLine = False
                rowLength = len(row)
            elif (len(row) == rowLength):#otherwise remove void lines
                data_matrix.append(row)
        return data_matrix
    
