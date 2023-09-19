from functools import lru_cache
import time
'''
n, m = map(int, input().split(' '))
graph = []
for i in range(n):
    graph.append(list(map(int, input().split(' '))))
'''
n, m = 5, 5
graph = [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]


# 方法2
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
@lru_cache  # 记忆化搜索，dfs过程中很多点被重复遍历，经验证效果显著
def dfs(i,j):
    dis = 1
    for d in dir:
        nex_i = i + d[0]
        nex_j = j + d[1]
        if 0 <= nex_i < n and 0 <= nex_j < m and graph[nex_i][nex_j] < graph[i][j]:  # 只往更低处dfs
            dis = max(dis, dfs(nex_i, nex_j) + 1)  # 本层的距离是更深层的距离+1，然后从4个方向返回的本层距离中取最大值
    return dis  # 边界条件，若if语句一次都没进入，表明当前点是一个局部最低点，直接返回1


res = 1
t1 = time.time()
for i in range(n):
    for j in range(m):
        res = max(res, dfs(i, j))  # 对每个点都使用一次dfs，因为有@lru_cache去重，所以每个点最多只走了一遍
print((time.time()-t1)*1000)
print(res)

'''

#方法1

def dfs(i,j, pre,grid,dp):
    if i<0 or i == len(grid) or j <0 or j == len(grid[0]):
        return 0
    if pre <= grid[i][j]:
        return 0
    if dp[i][j] != 0:
        return dp[i][j]
    cur =0
    cur = max(cur, dfs(i-1,j,grid[i][j],grid,dp))
    cur = max(cur, dfs(i +1, j, grid[i][j], grid, dp))
    cur = max(cur, dfs(i, j-1, grid[i][j], grid, dp))
    cur = max(cur, dfs(i, j+1, grid[i][j], grid, dp))
    dp[i][j] = cur +1
    print(dp)
    return dp[i][j]

res = 1
dp = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        res = max(res,dfs(i,j,1001,graph,dp))
print(res)
'''
