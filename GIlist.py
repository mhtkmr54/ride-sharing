"""
creates output matrices Gd and Gt that give order of nodes based on closeness for all nodes
run using:
python GIlist.py <x>
<x> is dist or time, for spatial or temporal sorting respectively
"""
import numpy as np
import sys
argv=sys.argv[1]
D = np.loadtxt(argv[1]+'.txt')#use the dist or time matrice created by Floyd-Warshall algorithm
Gd=np.zeros([100,100])
for i in range(1,101):
	Gd[i-1]=np.argsort(D[i-1], kind='quicksort', order=None) +1 
if(argv=='dist'):
	np.savetxt('Gd.txt', Gd, fmt='%-3.0f') 
elif(argv=='time'):
	np.savetxt('Gt.txt', Gd, fmt='%-3.0f')
	
"""
to create output matrices Tlist and TimeTlist that can store list of taxis by closeness for each node
and temporal distance for each taxi to each node respectively
"""
def taxilist():
	#taxis = (np.random.rand(20)*100).astype(int)+1
	taxis = [81 ,69 ,30, 46, 59 ,30 ,6,1,52,78,26,97,39,99,10,41,17,74 ,31 ,56]#origin point for 20 taxis
	Tlist = np.zeros([100,20])
	t     = np.zeros([100,20])
	T = np.loadtxt('time.txt')#use time matrix
	for i in range(1,101):
		for j in range(0,20):
			t[i-1][j]=T[i-1][taxis[j]]
		Tlist[i-1] = np.argsort(t[i-1], kind='quicksort', order=None)
		t[i-1]=sorted(t[i-1])
	np.savetxt('Tlist',Tlist,fmt='%-3.0f')#save output
	np.savetxt('TimeTlist',t,fmt='%-3.0f')
taxilist()