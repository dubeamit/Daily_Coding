# An anagram of a string is another string that contains same characters, only the order of characters can be different.
# For example, "Listen" and “Silent” are anagram of each other.
def anagram(s1,s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if len(s1) != len(s2):
        return False
    dictionary = {}
    for letter in s1:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    for letter in s2:
        if letter in dictionary:
            dictionary[letter] -= 1
        else:
            dictionary[letter] = 1
    for i in dictionary:
        if dictionary[i] != 0:
            return False
    return True


print('Are "Listen" and "silent" anagram of each other:-', anagram('Listen','Silent'))
print('Are "abcd" and "efcg" anagram of each other:-', anagram('abcd','efcg'))