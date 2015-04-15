import csv
from random import *
from math import *
from normalizationTP3 import Normalizer
class KMeanClusterer():

	
	def getClusterNumber(self):
		return self.k

	def getCluster(self,i):
		#print("lg " + str(len(self.clusters)) + " i" + str(i))
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
		tot = 0
		for cluster in self.clusters:
			tot = tot + len(cluster.getObservations())
		#print("avant assignement tot : "+str(tot))
		if len(self.getCluster(0).getObservations()) == 0:
			fini = False
			self.init_assignement()
		else:
			for cluster in self.clusters:	
				for observation in cluster.getObservations():
					#print(str(observation))
					targetCluster = self.findNearestCluster(observation)
					#print str(k)
					if targetCluster != cluster:  
					#print("obs a enlever" +str(observation))
					#print("; obs enlevee " + str(cluster.removeObservationAt(k)))
						#print observation
						cluster.removeObservation(observation)
						tot = 0
						for cluster in self.clusters:
							tot = tot + len(cluster.getObservations())
					#	print("normalement 149 tot : "+str(tot))
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
		pass

	def __init__(self,k,datafile):
		norm = Normalizer()
       	        data = norm.load_csv(datafile)
       	        self.clusters = []
       	        self.data_matrix = [data[i:i+k] for i in range(0,len(data), k)]
       	        for i in range(0,k):
			l = randint(0,len(self.data_matrix[i])-1)
			self.clusters.append(Cluster(self.data_matrix[i][l]))
       	        self.k = k
       	        
       	      #  for i in xrange(0, len(iris_data_matrix),k):
	
	def init_assignement(self):
			#print (str(observations[pos][0]))
		for cluster in self.data_matrix:
			for obs in cluster:
			      targetCluster = self.findNearestCluster(obs)
			      targetCluster.addObservation(obs)
			#self.clusters.append(Cluster(centroid[i], observations[i]))

		

class Cluster():
	
	def getObservations(self):
		return self.observations

	def getCentroid(self):
		return self.centroid
	      
	def removeObservation(self,observation):
		"""newtab = []
		for line in self.observations:
			if line != observation:
				newtab.append(line)
		if len(newtab) == len(self.observations):
			print("pb")
		else:
			print("pas de pb")
		self.observations = list(newtab)"""
		self.observations.remove(observation)
		
		
	def addObservation(self, observation):
		self.observations.append(observation)
		
	def setObservations(self,observations):
		self.observations = list(observations)

	def __init__(self, centroid):
		self.centroid = centroid
		self.observations = []



