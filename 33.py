n,m = map(int,input().split(' '))
grid = []
for i in range(n):
    grid.append(input())

dp = [[(-1,-1)]*m for _ in range(n)] #记录拐弯次数以及上一次的方向
if grid[0][1] == '.':
    dp[0][0] = (0,0)
if grid[1][0] == '.':
    dp[1][0] = (0,2)
if grid[1][1] == '.':
    dp[1][1] = (0,1)

for i in range(0,n):
    for j in range(0,m):
        if (i,j) != (0,0) or (0,1) or (1,0):
            if
            a = dp[i-1][j][0] if dp[i-1][j][1] == 2 else a = dp[i-1][j][0] + 1
            b = dp[i][j-1][0] if dp[i][j-1][1] == 0 else a = dp[i][j-1][1] + 1
            a = dp[i - 1][j-1][0] if dp[i - 1][j][1] == 1 else a = dp[i - 1][j-1][0] + 1
            dp[i][j] = []

