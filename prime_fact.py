# Finding prime factors of a given number
# eg 36 --> 2*2*3*3
# eg 15 --> 3*5


def prime_fact(n):
    factors = []
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            while n % i == 0:
                factors.append(i)
                n = n // i
    if n != 1:
        factors.append(n)
    return factors

print(prime_fact(15))