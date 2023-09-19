#法二：并查集，反向增加节点，只找是否有长度为k的公共字串
'''
n,k = map(int,input().split(' '))
words= []
for i in range(n):
    words.append(input())
del_node = list(map(int,input().split(' ')))
'''
n,k = 3,2
words = ['aba','cba','cbc']
del_node = [2,1,3]

def get_max_sub(str1,str2): #计算最大公共字串长度
    m,n = len(str1),len(str2)
    dp = [[[0]for _ in range(2)]*(n+1) for i in range(m+1)] #dp[i][j]表示str1前i和str2前j最长公共字串的的位置[l,r]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]