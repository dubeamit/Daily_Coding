# Given a word or phrase, check if it is isogram or not. An Isogram is a word in which no letter occurs more than once.
# Input : Machine
# Output : True
# "Machine" does not have any character repeating, 
# it is an Isogram

# Input : Geek
# Output : False
# "Geek" has 'e' as repeating character, 
# it is not an Isogram

def is_isogram(word):
    word = word.lower()
    iso = set()
    for i in word:
        # skip if special character
        if not i.isalpha(): 
            continue
        if i not in iso:
            iso.add(i)
        else:
            return False
    return True


print("Machine is isogram",is_isogram("Machine"))
print("Geek is isogram",is_isogram("Geek"))