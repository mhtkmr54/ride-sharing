"""
creates a sample input that can be fed to FloydWarshall.py

run using:
python DTinpwriter.py <x>
x is T or D, for temporal and spatial distances respectively

file ouput structure is:
no. of nodes(V)
no. of arcs(E)
<tail node> <head node> <weight>        --this line occurs E times
"""
import numpy as np
import sys
argv = sys.argv[1]
f = open("inp"+argv+".txt","w")
f.write('100\n')#no. of nodes
f.write('360\n')#no. of arcs
for i in range(1,101):
	if(i%10 !=0):#create arc to right
		a = int(np.random.rand()*10)
		f.write( str(i) + ' ' + str(i+1) + ' ' + str(a)+'\n' )
		f.write( str(i+1) + ' ' + str(i) + ' ' + str(a)+'\n' )#reverse direction
	if(i<91):#create arc down
		a = int(np.random.rand()*10)
		f.write( str(i) + ' ' + str(i+10) + ' ' + str(a)+'\n' )
		f.write( str(i+10) + ' ' + str(i) + ' ' + str(a)+'\n' )#reverse direction
f.close()