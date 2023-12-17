# Find the fibonaci series using recursive method

maxi = 100
def fib(n1,n2):
    result = n1 + n2
    print(result)
    if result < maxi:
        fib(n2,result)

fib(0,1)


