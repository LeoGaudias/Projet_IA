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

    def testKMeanInitialisation(self):
        print("** test KMean Initalisation **")
        
        k = 3 #nb classes
        datafile = "iris.csv"
        
        # perform initialization
        kMeanClusterer = KMeanClusterer(k, datafile)
        
        # check the number of clusters
        clusterNumber = kMeanClusterer.getClusterNumber()
        self.assertTrue(clusterNumber == k, "actual cluster number: " + str(clusterNumber) + "; expected: " + str(k))
        
        # check the consistency of each cluster
        centroids = set()
        for i in range(clusterNumber):
            currentCluster = kMeanClusterer.getCluster(i)
            # check centroid format
            centroid = currentCluster.getCentroid()
            expectedObsDimensions = 5
            self.assertTrue(len(centroid) == expectedObsDimensions,
                            "centroid expected to contain " + str(expectedObsDimensions) + 
                            " data items, has actually " + str(len(centroid)))
            # check observation format
            observations = currentCluster.getObservations()
            self.assertTrue(len(observations) == 0, "0 observation expected per cluster, has actually "
                            + str(len(observations)))
            
            # check all centroid are different at initialisation
            new_centroid = False
            if tuple(centroid) not in centroids:
                new_centroid = True
                centroids.add(tuple(centroid))
            self.assertTrue(new_centroid, "centroid are different: " + str(new_centroid))
        

    def testKMeanAssignement(self):
        print("** test KMean assignement **")
        
        # perform initialization
        k = 3
        datafile = "iris.csv"
        
        kMeanClusterer = KMeanClusterer(k, datafile)
       
        datasetSize = self.getDatasetSize(datafile)
        
        kMeanClusterer.assignement()
        
        obsNumber = 0
        clusterNumber = kMeanClusterer.getClusterNumber()
        print("clusternumber = "+str(clusterNumber))
        for i in range(clusterNumber):
	    print(str(i)+ " k")
            currentCluster = kMeanClusterer.getCluster(i)
            observations = currentCluster.getObservations()
            for obs in observations:
                obsNumber += 1

        # check that all observations are assigned
        self.assertTrue(datasetSize == obsNumber, "size of dataset: " + str(datasetSize)
                        + "; current number of observations in cluster:" + str(obsNumber))
        
        # check that the observations are assigned to the nearest centroid
        centroids = []
        for i in range(clusterNumber):
            currentCluster = kMeanClusterer.getCluster(i)
            centroids.append(currentCluster.getCentroid())
        
        for i in range(clusterNumber):
            currentCluster = kMeanClusterer.getCluster(i)
            for obs in currentCluster.getObservations():
                distance_to_centroid = kMeanClusterer.computeDistance(obs, currentCluster.getCentroid())
                for j in range(len(centroids)):
                    if i != j:
                        dst = kMeanClusterer.computeDistance(obs, kMeanClusterer.getCluster(j).getCentroid())
                        self.assertTrue(distance_to_centroid <= dst,
                                        "distance to centroid of own cluster " + str(i) + ":"
                                        + str(distance_to_centroid) + "; distance to centroid of cluster" + str(j) + ": " + str(dst)+ "own centroid : "+ str(currentCluster.getCentroid())
                                        + " the other centroid " + str(kMeanClusterer.getCluster(j).getCentroid()) + " the value : "+ str(obs) + "nb obs tot "+ str(len(kMeanClusterer.getCluster(0).getObservations())+len(kMeanClusterer.getCluster(1).getObservations())+len(kMeanClusterer.getCluster(2).getObservations())))
        

if __name__ == "__main__":
    unittest.main()
