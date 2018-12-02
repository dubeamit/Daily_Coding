# given a string print the frequency of each character.
# eg: aAbb ----> a1A1b2
def char_frequency(string):
    for _ in range(len(set(string))):
        print(string[0]+str(string.count(string[0])),end='')
        string = string.replace(string[0],'')
    print()

char_frequency('aaaabbBcddee')
char_frequency('aazzZ')