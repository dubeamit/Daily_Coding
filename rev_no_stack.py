# Reverse a number using stack
# Input : 365 --> Output : 563;  Input : 6899 --> Output : 9986

def rev_no_stack(num):
    stack = []  # using list as stack dataStructure
    while num:
        stack.append(num%10)
        num = num // 10
    i = 1
    rev = 0
    while stack:
        rev += stack.pop() * i
        i *= 10
    print(rev)

rev_no_stack(365)
rev_no_stack(6899)