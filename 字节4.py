n = int(input())
s = list(map(int,list(input())))

dp = [[[0,-1,0] for i in range(n)] for j in range(n)]
for i in range(n):
    dp[i][i] = [1,1,1]

for i in range(n):
    for j in range(i+1,n):
        if s[j]!=s[j-1]:
            dp[i][j][0] = dp[i][j-1][0]
            dp[i][j][1] = 0
            dp[i][j][2] = 1
        else:
            if dp[i][j-1][1] == 1:
                dp[i][j][0] = dp[i][j-1][0] + 1
                dp[i][j][1] = 1
                dp[i][j][2] = dp[i][j-1][1] + 1
            else:
                if dp[i][j-1][2] + 1 >= dp[i][j-1][0]:
                    dp[i][j][0] = dp[i][j-1][2] + 1
                    dp[i][j][1] = 1
                else:
                    dp[i][j][0] = dp[i][j - 1][0]
                    dp[i][j][1] = 0
                dp[i][j][2] = dp[i][j - 1][2] + 1
sum_value = 0
for i in range(n):
    for j in range(i,n):
        sum_value+=dp[i][j][0]
print(dp)
print(sum_value)
