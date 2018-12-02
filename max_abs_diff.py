# You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
# f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
# For example,
# A=[1, 3, -1]
# f(1, 1) = f(2, 2) = f(3, 3) = 0
# f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
# f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
# f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5
# So, we return 5.

def max_abs_diff(A):
	if not A:
		return 0
	else:
		N = len(A)
		mx1, mx2, mx3, mx4 = [-10**15] * 4
		for i in range(N):
			mx1 = max(mx1, A[i] + i)
			mx2 = max(mx2, - A[i] + i)
			mx3 = max(mx3, A[i] - i)
			mx4 = max(mx4, -A[i] - i)
		ans = -10**15
		for i in range(N):
			ans = max(ans, mx1 - A[i] - i)
			ans = max(ans, mx2 + A[i] - i)
			ans = max(ans, mx3 - A[i] + i)
			ans = max(ans, mx4 + A[i] + i)
		return ans

print(max_abs_diff([1,3,-1]))