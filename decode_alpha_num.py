def helper_dp(data, k, memo):
    if k == 0:
        return 1
    s = len(data) - k
    if data[s] == '0':
        return 0
    if memo[k] is not None:
        return memo[k]
    result = helper_dp(data, k-1, memo)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result += helper_dp(data, k-2, memo)
    memo[k] = result
    return result

def num_ways_dp(data):
    memo = [None]*(len(data)+1)
    return helper_dp(data, len(data), memo)

print(num_ways_dp('12'))
# should return two AB or L