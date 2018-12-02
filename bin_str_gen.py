# Generate all binary strings from given pattern
# Given a string containing of ‘0’, ‘1’ and ‘?’ wildcard characters, 
# generate all binary strings that can be formed by replacing each wildcard character by ‘0’ or ‘1’.

def bin_str_gen(patt):
    if '?' not in patt:
        print(patt,end='   ')
    else:
        bin_str_gen(patt.replace('?','0',1))
        bin_str_gen(patt.replace('?','1',1))

print()
bin_str_gen('1?1')
print('\n')
bin_str_gen('1??0?101')
print('\n')