t = int(input())
bridge = []
for i in range(t):
    bridge.append(list(map(int,input().split(' '))))

def get_ans(n,a,b):
    tmp = abs(a-b)
    re = n-1-tmp
    if re <0: return -1
    return max(a,b) + re//2

for data in bridge:
    print(get_ans(data[0],data[1],data[2]))