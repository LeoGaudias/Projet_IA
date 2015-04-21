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
        data = open(dataFile, 'r')
        for line in data:
            line = str.strip(line)
            print(line)

    def show_matrix_dataset(self, iris_data_matrix):
        print("Show matrix dataset")
        for row in iris_data_matrix:
            print(row)

    def load_csv(self, dataFile, values):
        # print("Load CSV from "+dataFile)
        
        data_matrix = []
         
        data = open(dataFile, 'r')
        firstLine = True
        rowLength = 0
        for row in data:
            columns = row.split(',')
            if firstLine:  #remove column names
                firstLine = False
                rowLength = len(row)
            elif (len(row) == rowLength):  #otherwise remove void lines
                tab = []
                for column in values:
                    if int(column) not in [2, 3, 4, 41]:
                        tab.append(columns[int(column)])

                data_matrix.append(tab)  # temporaire
        return data_matrix
