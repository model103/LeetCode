n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,list(input()))))
row = len(arr)
col = len(arr[0])

res = 0
for r in range(row):
    cur = 0
    j = 1
    while cur + j <= col:
        if cur + j != col and arr[r][cur] == arr[r][cur + j]:
            j += 1
        else:
            res += (j-1)*j
            cur += j
            j = 1

for c in range(col):
    cur = 0
    j=1
    while cur+j <= row:
        if cur+j !=row and arr[cur][c] == arr[cur+j][c]:
            j+=1
        else:
            res+=(j-1)*j
            cur +=j
            j = 1
print(res)