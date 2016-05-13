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

G_origin = new_query.pick
G_destination = new_query.des
S_origin = set()
S_destination = set()
Selected_taxis = S_origin | S_destination 
#intersection
l_o = []


    