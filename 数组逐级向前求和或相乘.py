a = list(map(int,input().split(' ')))

def updata_dp(dp,x):
    new_dp = [0]*10
    for i in range(10):
        if dp[i] != 0:
            new_dp[i*x%10]+=dp[i]
            new_dp[(i+x)%10]+=dp[i]
    return new_dp

l = len(a)
dp = [0]*10
dp[a[-1]%10] = 1
for i in range(l-2,-1,-1):
    dp = updata_dp(dp,a[i])

print(' '.join(str(i)for i in dp))