import matplotlib.pyplot as plt
from numpy.random import rand
from numpy import square, sqrt
def regionQuery(P, eps, D):	
	neighbourPts = []
	for point in D:
		#print point		
		if sqrt(square(P[1] - point[1]) + square(P[2] - point[2]))<eps:
			neighbourPts.append(point)

	return neighbourPts

def DBSCAN(D, eps, MinPts):
	noise = []
	visited = []
	C = []
	c_n = -1
	for point in D:
		visited.append(point) #marking point as visited
	#	print point		
		neighbourPts = regionQuery(point, eps, D)
		if len(neighbourPts) < MinPts:
			noise.append(point)
		else:
			C.append([])			
			c_n+=1
			expandCluster(point, neighbourPts, C, c_n,eps, MinPts, D, visited)

	print "no. of clusters: " , len(C)	
	print "length of noise:", len(noise)
	for cluster in C:
		col =[rand(1),rand(1),rand(1)]		
		print cluster		
		plt.scatter([i[1] for i in cluster],[i[2] for i in cluster],color=col)
	plt.show()

		

def expandCluster(P, neighbourPts, C, c_n,eps, MinPts, D, visited):
	
	C[c_n].append(P)
	for point in neighbourPts:
		if point not in visited:
			visited.append(point) 
			neighbourPts_2 = regionQuery(point, eps, D)
			if len(neighbourPts_2) >= MinPts:
				neighbourPts += neighbourPts_2
		if point not in (i for i in C):
			C[c_n].append(point)
 
eps = input("enter eps")

x=100*rand(1000)
y=100*rand(1000)
l=[]
for i in range(1000):
	l.append([i,x[i],y[i]])

DBSCAN(l,eps,30)

#print l[1]


