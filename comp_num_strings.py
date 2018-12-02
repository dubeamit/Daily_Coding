#compare two strings(s1,s2) as numbers and return True if s1>s2 else return False (cannot convert to int)
#eg: larger_than('334', '333')--> True
#eg: larger_than('525','6666')--> False
#eg: larger_than('11','0') --> True
#eg: larger_than('10','10') --> False

def larger_than(s1, s2):
    if len(s1) > len(s2):
        return True
    elif len(s1) < len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        elif s1[i] > s2[i]:
            return True
        else:
            return True        
    return False

print(larger_than('123','122'))