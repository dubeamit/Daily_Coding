# Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. 
# A and P both should be integers

def power(A):
    if A <= 1:
        return 1
    for x in range(2, int((A**0.5)+1)):
        p = x
        while p <= A:
            p *= x
            if p == A:
                return 1
    return 0

print(power(100))
print(power(729))
print(power(444444))