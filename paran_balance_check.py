# Balanced parenthesis check
# eg () --> True; eg )(--> False; eg [(])--> False
def paran_balance_check(s):
	stack = []
	if len(s)%2 != 0:
		return False
	opening = set('{([')
	matches = set([('(',')'),('[',']'),('{','}')])
	for paren in s:
		if paren in opening:
			stack.append(paren)
		else:
			if len(stack) == 0:
				return False
			last_open = stack.pop()
			if(last_open,paren) not in matches:
				return False
	return len(stack)==0

print(paran_balance_check('([{]})'))