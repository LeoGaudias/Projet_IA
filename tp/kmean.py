#!/usr/bin/env python3
import csv
from random import *
from math import *
from normalizationTP3 import Normalizer
class KMeanClusterer():

	
	def getClusterNumber(self):
		return self.k

	def getCluster(self,i):
		if(len(self.clusters) == 0):
		    return 0
		else:
		    return self.clusters[i]
    
	def findNearestCluster(self,observation):
		pluspetitedistance=  self.computeDistance(observation, self.getCluster(0).centroid)
		pos = 0
		for i in range(0,self.k):
		  
			distance = self.computeDistance(observation, self.getCluster(i).getCentroid())
			if distance< pluspetitedistance:
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
	      
	def computeDistance(self,obs,centroid):
		distance = 0
		#len - 1 pour ne pas prendre le nom de la classe
		for i in range(0,len(obs)-1):
			
			distance = distance + pow((float(obs[i])-float(centroid[i])),2)
		return sqrt(distance)
	      
	      
	def performClustering(self):
		while self.assignement() == False:
			self.update()
	      
	def update(self):
		for i in range(0,self.getClusterNumber()):
		    currentCluster = self.getCluster(i)
		    currentCluster.meanCentroid()

	def __init__(self,k,datafile):
		norm = Normalizer()
		data = norm.load_csv(datafile)
		self.clusters = []
		#self.data_matrix = [data[i:i+k] for i in range(0,len(data), k)]
		self.data_matrix = list(self.split(data, k))
		#print (self.data_matrix[0])
		for i in range(0,k):
			l = randint(0,len(self.data_matrix[i])-1)
			self.clusters.append(Cluster(self.data_matrix[i][l]))
		self.k = k
		
	def split(self,a, n):
		k, m = len(a) / n, len(a) % n
		return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in xrange(n))
		

class Cluster():
	
	def getObservations(self):
		return self.observations

	def getCentroid(self):
		return self.centroid
	      
	def removeObservation(self,observation):
		self.observations.remove(observation)
		
	def addObservation(self, observation):
		self.observations.append(observation)
		
	def setObservations(self,observations):
		self.observations = list(observations)
		
	def meanCentroid(self):
		mean = [0]*(len(self.centroid)-1)
		if len(self.observations) >0:
		      for obs in self.observations:
			    for i in range(0,len(obs)-1): #ne pas prendre le nom de la classe
				  mean[i] += float(obs[i])
		      for i in range(0,len(obs)-1):
			    mean[i] = mean[i]/len(self.observations)
		      self.centroid = mean

	def __init__(self, centroid):
		self.centroid = centroid
		self.observations = []



