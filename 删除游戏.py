N = 10**5+1
cnt = [0]*(N) #每个数的出现次数
n = int(input())
a = map(int,input().split())
for i in a:
 cnt[i] += 1
dp = [[0]*(N), [0]*(N)]

for i in range(1, N):
 dp[0][i] = max(dp[0][i-1], dp[1][i-1])
 dp[1][i] = dp[0][i-1] + i*cnt[i]
print(dp[0][N-1])