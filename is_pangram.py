# Pangram is a sentence using every letter of a given alphabet at least once.\
# eg: The quick brown fox jumps over the lazy dog
# eg: The five boxing wizards jump quickly

def is_pangram(sentence):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in letters:
        if letter not in sentence.lower():
            return False
    return True

print(is_pangram("The five boxing wizards jump quickly"))