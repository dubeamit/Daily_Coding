# Given a square matrix, calculate the absolute difference between the sums of its diagonal
# eg: 1 2 3
#     5 6 7
#     9 8 0
# |(1+6+0)-(3+6+9)| = 11

def abs_diff_mat(mat):
	sum1 = sum2 = i = 0
	for j in range(len(mat)-1,-1,-1): # range(2,-1,-1)-->(2,1,0)
		sum1 += mat[i][i]
		sum2 += mat[i][j]
		i += 1
	total = sum1 - sum2
	print(abs(total))

mat = [[11,2,4],[4,5,6],[10,8,-12]]
abs_diff_mat(mat)