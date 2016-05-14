# ride-sharing
App based ride sharing algorithms

The entire work has been split into 3 parts:
All parts are run in systematic order using the shellcomand.sh file, which is the primary executable

part I:(done in python)
System Initialisation:
1:A sample node network is created using DTinpwriter.py(inpT.txt and inpD.txt) that feeds into FloydWarshall.py.
  You can create your own custom input for FloydWarshall.py also.
2:FloydWarshall gives node-node distance for all nodes(dist.txt and time.txt), which is futher processed to get
  Gt.txt, Gd.txt Tlist, TimeTList.txt
3: These six matrices are utilized in the subsequent parts, and are pre computed to save running time

part II:(done in python)
Taxi Searching:
1:It uses the dual side searching algorithm to find suitable taxis to go from one node to another, for a query

part III:(done in Java)
Insertion Feasibility:
1:algorithm to check if it is poossible to add a query to existing taxi schedules, and,if yes, 
  to find the best insertion possible 