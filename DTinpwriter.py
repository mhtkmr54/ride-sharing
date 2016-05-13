import numpy as np

f = open("inpT.txt","w")
for i in range(1,101):
	if(i%10 !=0):
		a = int(np.random.rand()*10)
		f.write( str(i) + ' ' + str(i+1) + ' ' + str(a)+'\n' )
		f.write( str(i+1) + ' ' + str(i) + ' ' + str(a)+'\n' )
	if(i<91):
		a = int(np.random.rand()*10)
		f.write( str(i) + ' ' + str(i+10) + ' ' + str(a)+'\n' )
		f.write( str(i+10) + ' ' + str(i) + ' ' + str(a)+'\n' )
f.close()