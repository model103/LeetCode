n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split(' '))))
size = n
while size > 1:
    new_arr = []
    for i in range(0,size,2):
        one_row = []
        for j in range(0,size,2):
            one_row.append(sorted(arr[i][j:j+2] + arr[i+1][j:j+2])[-2])
        new_arr.append(one_row)
    arr = new_arr
    size = size // 2

print(arr[0][0])