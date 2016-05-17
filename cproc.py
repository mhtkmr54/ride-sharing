def fibo_rec(n):
    if n <= 1:
        return n
    else:
        print "sdada" 
        return fibo_rec(n-2) + fibo_rec(n-1)
        

if __name__ == "_main_" :
    import cProfile
    cProfile.run('fibo_rec(100)')
    
	
