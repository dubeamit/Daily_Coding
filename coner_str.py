# Find if a string starts and ends with another given string
def coner_str(s, cs):
    if len(s) < len(cs):
        return False
    if s[0] == cs[0] and s[len(s)-1] == cs[len(cs)-1]:
        return True
    return False

print(coner_str("geeksmanishgeeks","geeks"))
print(coner_str('shreya dhatwalia', 'abc'))