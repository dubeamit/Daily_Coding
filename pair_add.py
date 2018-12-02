# Given a list and a no. k return whether any two nos. from the list add up to k
# [10,15,3,7] k = 17 --> return True since 10+7 = 17
# [-10,0,20,30,34], k = 10 --> return True since -10+20 = 10

def pair_add(lst, k):
	if len(lst) < 2:
		return False
	numbers_seen = {} #dictionary
	for i in lst:
		if k-i in numbers_seen:
			print(str(k-i)+', '+str(i))
			return True
		else:
			numbers_seen[i] = 1
	return False	

print(pair_add([-10,0,20,30,34],10))