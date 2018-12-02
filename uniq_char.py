# RETURN THE UNIQUE CHARACTERS IN A GIVEN ARRAY/LIST
def uniq_char(string):
    dictionary = {}
    for char in string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    
    for key in dictionary:
        if dictionary[key] == 1:
            print(key,end=' ')
    print()

print('The unique characters are')
uniq_char('aaaaccdddexyyy')
uniq_char('aabccdd')