n,m = map(int,input().split(' '))
g = []
for i in range(n):
    g.append(input())

def minstep(g,n,m):
    dp = [[float('inf')]*m for _ in range(n)]
    dp[0][0] = 0 if g[0][0] == '.' else float('inf')

    for i in range(n):
        for j in range(m):
            if g[i][j] == '.':
                for k in range(1,i+1):
                    if i > 0:
                        if g[i-k][j] == '.':
                            dp[i][j] = min(dp[i][j],dp[i-k][j] + 1)
                        else: break
                for k in range(1, j+1):
                    if j>0:
                        if g[i][j-k] == '.':
                            dp[i][j] = min(dp[i][j],dp[i][j-k] + 1)
                        else:
                            break
                for k in range(1, min(i+1,j+1)):
                    if i>0 and j>0:
                        if g[i-k][j-k] == '.':
                            dp[i][j] = min(dp[i][j],dp[i-k][j-k] + 1)
                        else:
                            break
    return dp[n-1][m-1] if dp[n-1][m-1] != float('inf') else -1

res = minstep(g,n,m)
print(res)
