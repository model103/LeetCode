#小欧拿到了一个数组，她每次随机选择一个元素，然后将该元素以及其后缀全部删除。已知第i个元素a_i被选到的概率为a_i/sum，其中sum为当前数组所有元素之和。
#小欧想知道，将数组全部删完的期望次数是多少?
#输入描述
#第一行输入一个正整数n，代表数组的大小
# 第二行输入n个正整数a，代表数组的元素
#1<n<100 1<ai <10^9
#示例:
# 输入:
# 2
# 1 3
# 输出:1.75
#说明:25%的概率操作1次，75%的概率操作2次，总期望次数为1*0.25+2*0.75=1.75
def calculate_expectation(n, arr):
    dp = [[0]*(n+1) for i in range(n+1)] #dp[i][j]表示第i步消除后还余下j长度的序列的概率
    dp[0][n] = 1  #开始消除前长度为n的概率为1
    for i in range(1,n+1):
        for j in range(0,n-i+1): #第i次消除后长度不可能超过n-i
            for k in range(j+1, n-i+2): #上一次(i-1次)消除后剩长度k，其大于j，小于等于n-i+1
                p = arr[j]/sum(arr[:k])#长度为k的情况下经过一次消除后长度为j的概率
                dp[i][j] += dp[i-1][k]*p #全概率公式
    e = 0  #期望步数
    for i in range(1,n+1):
        e += i*dp[i][0] #第i步*第i步消到0长度
    return e

n = 2
arr = [1,3]

e = calculate_expectation(n, arr)
print(e)
