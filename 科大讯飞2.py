from collections import defaultdict

n = int(input())
m = int(input())
dis = defaultdict(int)
graph = defaultdict(list)
for i in range(m):
    tmp = list(map(int, input().split(' ')))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])
    dis[(tmp[0],tmp[1])] = tmp[2]
    dis[(tmp[1], tmp[0])] = tmp[2]
d = int(input())
none_road = set()
print(i)
for i in range(d):
    none_road.add(tuple(map(int, input().split(' '))))

a,b = map(int,input().split(' '))
print(graph)
def findAllPath(graph,start,end):
    path=[]
    stack=[]
    stack.append(start)
    visited=set()
    visited.add(start)
    seen_path={}
    while (len(stack)>0):
        start=stack[-1]
        nodes=graph[start]
        if start not in seen_path.keys():
            seen_path[start]=[]
        g=0
        for w in nodes:
            if w not in visited and w not in seen_path[start]:
                g=g+1
                stack.append(w)
                visited.add(w)
                seen_path[start].append(w)
                if w==end:
                    path.append(list(stack))
                    old_pop=stack.pop()
                    visited.remove(old_pop)
                break
        if g==0:
            old_pop=stack.pop()
            del seen_path[old_pop]
            visited.remove(old_pop)
    return path

all_path = findAllPath(graph,a,b)
print(all_path)
print(none_road)
adds = []
for path in all_path:
    add = 0
    for i in range(len(path)-1):
        if (path[i],path[i+1]) in none_road or (path[i+1],path[i]) in none_road:
            add += dis[(path[i],path[i+1])]
    adds.append(add)
print(min(adds))

