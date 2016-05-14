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
S_origin = set()
S_destination = set()
Selected_taxis = S_origin | S_destination 
#intersection
l_o = []

T_sorted = [[]]
T = [[]]
for grid_cell in T_sorted[G_origin]:
    if new_query.curr_time + T[int(grid_cell)][G_origin] < new_query.curr_time + 6 :
        l_o.append(grid_cell)
    else:
        break
    
l_d = []
for grid_cell in T_sorted[G_destination]:
    if new_query.curr_time + T[int(grid_cell)][G_destination] < T[G_origin][G_destination] + 6 :
        l_d.append(grid_cell)
    else:
        break
    
Stop_O = False
# stop flag for origin side searching
Stop_D = False
#stop flag for destination side searching
i = 1
while len(Selected_taxis) and Stop_O == False or Stop_D == False :
    For taxi in Tlist[G_origin]:
        if taxi >= new_query.curr_time and taxi < new_query.curr_time + 6 :
            S_origin.add(taxi)
        else:
            break
            
    For taxi in Tlist[G_destination]:
        if taxi >= new_query.curr_time and taxi < T[G_origin][G_destination] + 6 :
            S_destination.add(taxi)
        else:
            break
    
    if len(Selected_taxis):
        break
    
    #-------------------------------------------------------------------------------------
    For taxi in Tlist[l_o[i]]:
        if taxi >= new_query.curr_time and taxi < (new_query.curr_time + 6) - Time[l_o[i]][G_origin] :
            S_origin.add(taxi)
        else:
            break
            
    For taxi in Tlist[l_d[i]]:
            if taxi >= new_query.curr_time and taxi < T[G_origin][G_destination] + 6 - Time[l_d[i]][G_destination]:
                S_destination.add(taxi)
            else:
                break
    
    if len(Selected_taxis):
        break
    
    i = i + 1
    
    
        
        
            
    