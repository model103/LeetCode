from collections import defaultdict,deque
n,k = map(int,input().split(' '))
words= []
for i in range(n):
    words.append(input())
del_node = list(map(int,input().split(' ')))
def get_max_sub(str1,str2): #计算最大公共字串长度
    m,n = len(str1),len(str2)
    dp = [[0]*(n+1) for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

#建立无向图
graph = defaultdict(list)
for i in range(n):
    for j in range(i+1,n):
        if get_max_sub(words[i],words[j]) >= k:
            graph[i].append(j)
            graph[j].append(i)

#bfs计算连通域数量
def get_connect_num(graph,del_set):
    visited = del_set.copy()
    unvisited = set(range(n)) - visited
    connect_num = 0
    q = deque()

    while unvisited:
        tmp = unvisited.pop()
        q.append(tmp)
        visited.add(tmp)
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if nxt not in visited:
                    q.append(nxt)
                    visited.add(nxt)
                    unvisited.remove(nxt)
        connect_num+=1
    return connect_num

del_set = set()
print(get_connect_num(graph,del_set))

for del_n in del_node:
    del_set.add(del_n-1)
    print(get_connect_num(graph,del_set))

'''
3 2
aba
cba
cbc
2 1 3
'''

