n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(float, input().split(' '))))
v0 = list(map(float, input().split(' ')))

def updatev(arr,v,n):
    newv = [sum([arr[i][j] * v[j] for j in range(n)]) for i in range(n)]
    return newv

last_ratio = [0]*n
while True:
    newv = updatev(arr,v0,n)
    new_ratio = [newv[i] / v0[i] for i in range(n)]
    delta = [abs(new_ratio[i] - last_ratio[i]) for i in range(n)]
    if max(delta) < 0.001:
        break
    v0 , last_ratio = newv, new_ratio
print(round(new_ratio[0],2))