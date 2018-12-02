# Memoization(top-down)
def fib(n, lookup):
    if n == 0 or n == 1:
        lookup[n] = n
    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
    return lookup[n]

def main():
    n = 6
    lookup = [None]*(n+1)
    fib(n,lookup)
    print('Fibonacci series is', lookup)

if __name__=='__main__':
    main()