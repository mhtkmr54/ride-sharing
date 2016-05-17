import profile

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_memo(n):
    memo = {}
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f = fib_memo(n-1) + fib_memo(n-2)
        memo[n] = f
        return f

print 'RAW'
print '=' * 80
profile.run('print fib_memo(30); print')
