n,m = map(int,input().split(' '))

v= []
w = []
for i in range(n):
    b,j = map(int,input().split(' '))
    v.append(j)
    w.append(j-b)

dp = [0]*(m+1)
for i in range(n):
    for j in range(m,v[i]-1,-1):
        dp[j] = max(dp[j],dp[j-v[i]] + w[i])

print(dp[-1])

