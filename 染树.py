n = int(input())
weight = list(map(int, input().split(' ')))
tree = [[] for _ in range(n)]
root = set([i for i in range(n)])  # 找根节点用的
color = [True] * n
for i in range(n - 1):
    par, son = map(int, input().split(' '))
    tree[par - 1].append(son - 1)
    root.discard(son - 1)

def is_squrt(i, j):
    dot = weight[i] * weight[j]
    if dot == int(dot ** 0.5) ** 2:
        return True
    return False

dp = [[0 for i in range(2)]]*n

def dfs(i):
    global nums
    for j in tree[i]:
        if color[j] and color[i]:
            if is_squrt(i, j):
                nums += 2
                color[i] = False
                color[j] = False
        dfs(j)

dp = [0]*n
dp[0] = 0
i=1
while i<2:

for node in tree:
    for son in node[i]:
        i +=1
        if i >2:
            if is_squrt(node, son):
                dp[i] = max(dp[i-2]+2,dp[i-1])
            else:
                dp[i] =dp[i-1]




dfs(root.pop())
print(nums)
