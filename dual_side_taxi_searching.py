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
        
new_query = Query((4,7,25))
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

for grid_cell in Gt[G_origin]:
    if new_query.curr_time + T[grid_cell][G_origin] < new_query.curr_time + time_window :
        l_o.append(grid_cell)
    else:
        break
    
l_d = []
for grid_cell in Gt[G_destination]:
    if new_query.curr_time + T[grid_cell][G_destination] < T[G_origin][G_destination] + time_window :
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
while len(Selected_taxis) == 0 and (Stop_O == False or Stop_D == False) :
    for taxi in Tlist[G_origin]:
        if TimeTlist[G_origin][taxi] >= new_query.curr_time and taxi < new_query.curr_time + time_window :
            S_origin.add(taxi)
        else:
            break
            
    for taxi in Tlist[G_destination]:
        if TimeTlist[G_destination][taxi] >= new_query.curr_time and taxi < T[G_origin][G_destination] + time_window :
            S_destination.add(taxi)
        else:
            break
    print Selected_taxis
    print "Selected_taxis above"
    if len(Selected_taxis):
        break
    
    #-------------------------------------------------------------------------------------
    try:
        for taxi in Tlist[l_o[i]]:
            if TimeTlist[l_o[i]][taxi] >= new_query.curr_time and taxi < (new_query.curr_time + time_window) - T[l_o[i]][G_origin] :
                S_origin.add(taxi)
            else:
                break
    except IndexError:
        pass
    
    try:       
        for taxi in Tlist[l_d[i]]:
            if TimeTlist[l_d[i]][taxi] >= new_query.curr_time and taxi < T[G_origin][G_destination] + time_window - T[l_d[i]][G_destination]:
                S_destination.add(taxi)
            else:
                break
    except IndexError:
        pass        
            
    if len(Selected_taxis):
        break
    i = i + 1
    
    
print Selected_taxis
    