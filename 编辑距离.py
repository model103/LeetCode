def minDistance(word1: str, word2: str) -> int:
    n1 = len(word1)
    n2 = len(word2)
    dp = [[[0]*4 for __ in range((n2 + 1))] for _ in range(n1 + 1)]  #[0]*4，第一个0表示总的修改次数，第二个0表示插入次数，第三个0删除次数，第四个0替换次数
    #初始化
    # 第一行
    for j in range(1, n2 + 1):
        dp[0][j][0] = dp[0][j - 1][0] + 1
        dp[0][j][1] = dp[0][j - 1][1] + 1
        dp[0][j][2] = dp[0][j - 1][2]
        dp[0][j][3] = dp[0][j - 1][3]
        # 第一列
    for i in range(1, n1 + 1):
        dp[i][0][0] = dp[i - 1][0][0] + 1
        dp[i][0][1] = dp[i - 1][0][1]
        dp[i][0][2] = dp[i - 1][0][2] + 1
        dp[i][0][3] = dp[i - 1][0][3]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j][0] = min(dp[i][j - 1][0], dp[i - 1][j][0], dp[i - 1][j - 1][0]) + 1
                #专门统计插入删除替换次数
                if dp[i][j][0] == dp[i][j - 1][0] + 1:  #是插入
                    dp[i][j][1] = dp[i][j - 1][1] + 1
                    dp[i][j][2] = dp[i][j - 1][2]
                    dp[i][j][3] = dp[i][j - 1][3]
                if dp[i][j][0] == dp[i-1][j][0] + 1:  #是删除
                    dp[i][j][1] = dp[i-1][j][1]
                    dp[i][j][2] = dp[i-1][j][2] + 1
                    dp[i][j][3] = dp[i-1][j][3]
                if dp[i][j][0] == dp[i-1][j - 1][0] + 1:  #是替换
                    dp[i][j][1] = dp[i-1][j - 1][1]
                    dp[i][j][2] = dp[i-1][j - 1][2]
                    dp[i][j][3] = dp[i-1][j - 1][3] + 1

    return dp[-1][-1]

print(minDistance('horse','ros'))
