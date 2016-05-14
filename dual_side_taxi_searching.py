import numpy as np

class Query(object):
    def __init__(self, query):
        #query = (curr_time,pick,des)
        curr_time,pick,des = query
        self.curr_time = curr_time
        self.pick = pick
        self.des = des
    
class Taxi(object):
    
    def _init_(self,status):
        #status = (query_array,loc)
        query_array,loc = status
        self.loc = loc 
        #grid cell to which it belongs
        self.query_array = query_array
        
    #def insert(self,query):
        
new_query = Query((4,7,2))
time_window = 6

G_origin = new_query.pick
G_destination = new_query.des
#set of taxis at origin
S_origin = set()
#set of taxis at destination
S_destination = set()
Selected_taxis = S_origin | S_destination 
#intersection of sets
l_o = []


T = np.loadtxt('time.txt')
#The temporally ordered grid list of grid cell g is  Gt
#The spatial ordered grid list of grid cell g is  Gt

Gt= np.loadtxt('Gt.txt')
Gd= np.loadtxt('Gd.txt')

for grid_cell in Gt[G_origin-1]:
    if new_query.curr_time + T[grid_cell][G_origin-1] < new_query.curr_time + time_window :
        l_o.append(grid_cell)
    else:
        break
    
l_d = []
for grid_cell in Gt[G_destination-1]:
    if new_query.curr_time + T[grid_cell-1][G_destination-1] < T[G_origin-1][G_destination-1] + time_window :
        l_d.append(grid_cell)
    else:
        break
    
print l_o
print l_d
    
Stop_O = False
# stop flag for origin side searching
Stop_D = False
#stop flag for destination side searching
Tlist=np.loadtxt('Tlist')
TimeTlist=np.loadtxt('TimeTlist.txt')
i = 1
check = 0

# initial check on origin grid and destination grid
for taxi in Tlist[G_origin-1]:
    if TimeTlist[G_origin-1][taxi] >= new_query.curr_time and taxi < new_query.curr_time + time_window :
        S_origin.add(taxi)
    else:
        break
            
for taxi in Tlist[G_destination-1]:
    if TimeTlist[G_destination-1][taxi] >= new_query.curr_time and taxi < T[G_origin-1][G_destination-1] + time_window :
        S_destination.add(taxi)
    else:
        break
    
print S_origin | S_destination
print "Selected_taxis above"
if len(S_origin | S_destination):
    check == 1


#cheking nearby cells of origin and destination
while len(S_origin | S_destination) == 0 and (Stop_O == False or Stop_D == False) :

    if check == 1:
        break
    
    #-------------------------------------------------------------------------------------
    try:
        for taxi in Tlist[l_o[i]-1]:
            if TimeTlist[l_o[i]-1][taxi] >= new_query.curr_time and taxi < (new_query.curr_time + time_window) - T[l_o[i]-1][G_origin-1] :
                S_origin.add(taxi)
            else:
                break
    except IndexError:
        pass
    
         
    for taxi in Tlist[l_d[i]-1]:
        if TimeTlist[l_d[i]-1][taxi] >= new_query.curr_time and taxi < T[G_origin-1][G_destination-1] + time_window - T[l_d[i]-1][G_destination-1]:
            S_destination.add(taxi)
        else:
            break
    print S_origin | S_destination
    print "Selected_taxis above from while loop"
    if len(Selected_taxis):
        break
    i = i + 1
    
    

    