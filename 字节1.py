def cal(n,k,a1,a2,a3):
    if 3*k>n:
        return -1
    p = [a1,a2,a3]
    p.sort()
    inti_dis1 = p[1]-p[0]
    inti_dis2 = p[2]-p[1]
    inti_dis3 = n - inti_dis1 - inti_dis2
    #print(inti_dis1,inti_dis2,inti_dis3)
    if inti_dis1>=k and inti_dis2>=k and inti_dis3>=k:
        return 0
    dis = [inti_dis1,inti_dis2,inti_dis3]
    dis.sort()
    if dis[1]>=k:
        return k-dis[0]
    return 2*k-dis[0] -dis[1]

t = int(input())
output = []
for i in range(t):
    n, k, a1, a2, a3 = map(int,input().split(' '))
    output.append(cal(n, k, a1, a2, a3))
for i in range(t):
    print(output[i])
