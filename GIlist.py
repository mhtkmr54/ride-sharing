import numpy as np
D = np.loadtxt('dist.txt')
Gd=np.zeros([100,100])
for i in range(1,101):
	Gd[i-1]=np.argsort(D[i-1], kind='quicksort', order=None) +1 
np.savetxt('Gd.txt', Gd, fmt='%-3.0f') 

def taxilist():
	#taxis = (np.random.rand(20)*100).astype(int)+1
	taxis = [81 ,69 ,30, 46, 59 ,30  ,6 , 1 ,52 ,78 ,26 ,97 ,39 ,99 ,10 ,41 ,17 ,74 ,31 ,56]
	Tlist = np.zeros([100,20])
	t     = np.zeros([100,20])
	T = np.loadtxt('time.txt')
	for i in range(1,101):
		for j in range(0,20):
			t[i-1][j]=T[i-1][taxis[j]]
		Tlist[i-1] = np.argsort(t[i-1], kind='quicksort', order=None)
		t[i-1]=sorted(t[i-1])
	np.savetxt('Tlist',Tlist,fmt='%-3.0f')
	np.savetxt('TimeTlist',t,fmt='%-3.0f')
taxilist()