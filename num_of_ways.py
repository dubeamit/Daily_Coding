# num of ways to climb staircase
# num of steps to take at any given point is 1 or 2 step
def num_of_ways(n):
    if n == 0 or n == 1:
        return 1
    table = [None]*(n+1)
    table[0] = 1
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

print(num_of_ways(4))
# 5 ways to climb