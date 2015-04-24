# coding=utf-8
import csv
from random import *
from math import *
from DetectionAnomalie.normalization import Normalizer

import json

class KMeanClusterer():
    def getClusterNumber(self):
        return self.k

    def getCluster(self, i):
        if (len(self.clusters) == 0):
            return 0
        else:
            return self.clusters[i]

    def findNearestCluster(self, observation):
        pluspetitedistance = self.computeDistance(observation, self.getCluster(0).centroid)
        pos = 0
        for i in range(0, self.k):

            distance = self.computeDistance(observation, self.getCluster(i).getCentroid())
            if distance < pluspetitedistance:
                pluspetitedistance = distance
                pos = i
        return self.getCluster(pos)

    def assignement(self):
        fini = True
        if len(self.getCluster(0).getObservations()) == 0:
            fini = False
            for cluster in self.data_matrix:
                for obs in cluster:
                    targetCluster = self.findNearestCluster(obs)
                    targetCluster.addObservation(obs)
        else:
            for cluster in self.clusters:
                for observation in cluster.getObservations():
                    targetCluster = self.findNearestCluster(observation)
                    if targetCluster != cluster:
                        cluster.removeObservation(observation)

                        targetCluster.addObservation(observation)
                        fini = False

        return fini

    def computeDistance(self, obs, centroid):
        distance = 0
        
        try:
            for i in range(0, len(obs)): 
                distance = distance + pow((float(obs[i]) - float(centroid[i])), 2)
        except(IndexError):
            pass
        return sqrt(distance)


    def performClustering(self):
        while self.assignement() == False:
            self.update()

    def update(self):
        for i in range(self.getClusterNumber()):
            currentCluster = self.getCluster(i)
            currentCluster.updateCentroid()

    def extractComportements(self,i):
        

        observations = []
        for obs in self.getCluster(i).getObservations():
            tab = []
            for val in obs:
                tab.append(val)
            observations.append(tab)

        for obs in observations:
            obs.append(self.computeDistance(obs, self.getCluster(i).getCentroid()))
        observations.sort(key=lambda colonnes: colonnes[-1])
        for obs in observations:
            obs.pop()
        n = int((self.n*len(observations))/100)
            
        return observations[:n]

    def extractValuesGraph(self):
        
        data = []
        
        for i in range(self.getClusterNumber()):
            cluster = self.getCluster(i)
            len_anomalie = len(self.extractComportements(i))
            len_normale = len(cluster.getObservations()) - len_anomalie
            
            data.append({"Cluster": str(i), "Observations anormales": str(len_anomalie),"Observations normales": str(len_normale)})
        return(json.dumps(data))
        
      

    def __init__(self, k, datafile, n, values):
        norm = Normalizer()
        data = norm.load_csv(datafile, values)
        self.clusters = []
        
        self.data_matrix = list(self.split(data, k))
        
        for i in range(0, k):
            l = randint(0, len(self.data_matrix[i]) - 1)
            self.clusters.append(Cluster(self.data_matrix[i][l]))
        self.k = k
        self.n = n


    def split(self,a, n):
        k, m = len(a) / n, len(a) % n
        return (a[int(i * k + min(i, m)):int((i + 1) * k + min(i + 1, m))] for i in range(n))


class Cluster():
    def getObservations(self):
        return self.observations

    def getCentroid(self):
        return self.centroid

    def removeObservation(self, observation):
        self.observations.remove(observation)

    def addObservation(self, observation):
        self.observations.append(observation)

    def setObservations(self, observations):
        self.observations = list(observations)

    def updateCentroid(self):
        mean = [0] * (len(self.centroid))  
        j = 0
        if len(self.observations) > 0:
            for obs in self.observations:  
                for i in range(len(obs)):  
                    mean[i] += float(obs[i])
                j += 1
            for i in range(len(obs)):  
                mean[i] /= len(self.observations)
            self.centroid = mean

    def __init__(self, centroid):
        self.centroid = centroid
        self.observations = []




