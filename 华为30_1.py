leaf_nums = int(input())
leaf_values = list(map(int,input().split(' ')))
dp = [[-float('inf'), float('inf')] for _ in range(2 * leaf_nums - 1)]  # dp[i][0]表示第i节点下的叶子最小值,dp[i][1]最大值
for i in range(leaf_nums):
    dp[i + leaf_nums - 1][0] = leaf_values[i]
    dp[i + leaf_nums - 1][1] = leaf_values[i]

def dfs(root): #树状dp
    if root<leaf_nums-1:
        dfs(2*root+1)
        dfs(2*root+2)
        dp[root][0] = min(dp[2*root+1][0],dp[2*root+2][0])
        dp[root][1] = max(dp[2 * root + 1][1], dp[2 * root + 2][1])
    else: return

dfs(0)

res = [(dp[0][0]+dp[0][1])//2] #当前节点的最终结果
par_sum = [(dp[0][0]+dp[0][1])//2] #储所有父节点（包括自身）的和
for i in range(1,2*leaf_nums-1):
    cur_res = (dp[i][0]+dp[i][1])//2 - par_sum[(i-1)//2]
    res.append(cur_res)
    par_sum.append(cur_res + par_sum[(i-1)//2])
print(' '.join(map(str,res)))




