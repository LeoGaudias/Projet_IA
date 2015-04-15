'''
Created on 24 mars 2015

@author: Pierre.Parrend
'''
import unittest

from normalizationTP3 import Normalizer
from kmean import KMeanClusterer


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def getDatasetSize(self, datafile):

        norm = Normalizer()
        iris_data_matrix = norm.load_csv(datafile)
        return len(iris_data_matrix)

    def testKMean(self):
        print("** test KMean **")
        
        # perform initialization
        k = 3
        datafile="iris.csv"
        kMeanClusterer = KMeanClusterer(k,datafile)
        kMeanClusterer.performClustering()
        
        #total number of lines in the dataset
        dataLines = 0
        norm = Normalizer()
        data_matrix = norm.load_csv(datafile)
        for row in data_matrix:
            if len(row) > 0:
                dataLines += 1

        #check the number of observations from dataset is kept        
        totalObsNb = 0
        for clusterNb in range(kMeanClusterer.getClusterNumber()):
            cluster = kMeanClusterer.getCluster(clusterNb)
            totalObsNb += len(cluster.getObservations())
        
        self.assertTrue(dataLines == totalObsNb, "Number of entries in dataset: "+str(dataLines)
                        +" is different from number of observations in cluster: "+str(totalObsNb))
        
        # check all entries in the dataset are kept
        index = 0
        for entry in data_matrix:
            found = False
            for clusterNb in range(kMeanClusterer.getClusterNumber()):
                cluster = kMeanClusterer.getCluster(clusterNb)
                observations = cluster.getObservations()
                for obs in observations:
                    if obs == entry:
                        found = True
            self.assertTrue(found, "observation "+str(entry)+" not found at index "+str(index))
            index += 1
            
    def testKMeanUpdate(self):
        print("** test KMean update **")
        
        k = 3
        datafile="iris.csv"
        kMeanClusterer = KMeanClusterer(k,datafile)
        
        kMeanClusterer.assignement()
        kMeanClusterer.update()
        
        # check existence of centroid
        for i in range(kMeanClusterer.getClusterNumber()):
            current_cluster = kMeanClusterer.getCluster(i)
            self.assertTrue(len(current_cluster.getCentroid()) > 0, "void centroid for cluster "+str(i))
        
        # check validity of centroid
        for i in range(kMeanClusterer.getClusterNumber()):
            current_cluster = kMeanClusterer.getCluster(i)
            current_centroid = current_cluster.getCentroid()
            obs = current_cluster.getObservations()
            for j in range(len(current_centroid)):
                tmp = 0
                for i in range(len(obs)):
                    try:
                        tmp += float(obs[i][j])
                    except ValueError:
                        pass # field is not numeric
                try:
                    value = float(current_centroid[j])#for test that data is numeric
                    self.assertTrue(tmp/len(obs) == value, "current centroid: "+str(value)
                                +"; actual centroid value: "+str(tmp/len(obs)))
                except ValueError:
                        pass # field is not numeric

    def testarray_equility(self):
        print("** test array equility **")
            
        a = [5.1, 3.5, 1.4, 0.2]
        b = [5.1, 3.5, 1.4, 0.2]
        self.assertTrue(a == b, "a not equal to b")

if __name__ == "__main__":
    unittest.main()