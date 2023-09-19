n = int(input())
a = []
b =[]

for i in range(n):
    d1,d2 = map(int,input().split(' '))
    a.append(d1)
    b.append(d2)
already = 0
need = sum(a)
res = 0
for i in range(0,need):
    max_num = max(b)
    idx = b.index(max_num)
    if i>= max_num:
        res+=1
    else:res+=2
    a[idx]-=1
    b[idx]-=1
    if a[idx] ==0:
        b[idx] =0
print(res)

