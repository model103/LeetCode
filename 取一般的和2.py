n = int(input())
ss = input().split(' ')
arr = list(map(int,ss))
'''
if ss[0].isdigit():
    arr.append(int(ss[0]))
arr+=map(int,ss[1:-1])
if ss[-1].isdigit():
    arr.append(int(ss[-1]))
#arr = list(map(int, input().split(' ')))
'''
total =sum(arr)
#cap = arr_sum//2


def count(nums):
    if n<2:
        return False
    maxnum = max(arr)
    total = sum(arr)
    if total &1:
        return False
    target = total//2
    if maxnum>target:
        return False
    dp = [[False]*(target+1) for _ in range(n)]
    for i in range(n):
        dp[i][0] = True
    dp[0][nums[0]] = True
    for i in range(1,n):
        num = nums[i]
        for j in range(1,target+1):
            if j>=num:
                dp[i][j] = dp[i-1][j] | dp[i-1][j-num]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n-1][target]
if count(arr):
    print('true')
else:print('false')

