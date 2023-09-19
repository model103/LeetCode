from collections import defaultdict
n = int(input())
needs = list(map(int,input().split()))
graph = defaultdict(list)
in_degree = [0]*n
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] ==1:
            graph[j].append(i)
            in_degree[i]+=1
def topo(n, graph, need,in_degree):
    zero_degree = set()
    for i in range(n):
        if in_degree[i] == 0:
            zero_degree.add(i)

    max_memory = 0
    while zero_degree:
        cur_need = 0
        nex = set()
        while zero_degree:
            q = zero_degree.pop()
            cur_need+=need[q]
            for j in graph[q]:
                in_degree[j]-=1
                if in_degree[j] == 0:
                    nex.add(j)
        max_memory = max(max_memory,cur_need)
        zero_degree = nex
    return max_memory

print(topo(n,graph,needs,in_degree))



