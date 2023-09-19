n = int(input())
init_sam = input()

m = int(input())
sub = []
add = []
for i in range(m):
    sub.append(input())
    add.append(input())

q = int(input())
eat = []
for i in range(q):
    eat.append(int(input())-1)

for i in range(q):
    a = []
    for j in range(n): #吃药后治好的情况
        if init_sam[j] == '0' and sub[eat[i]][j] == '0':
            a.append('0')
        if init_sam[j] == '1' and sub[eat[i]][j] == '0':
            a.append('1')
        if sub[i][j] == '1':
            a.append('0')
    new_samp = []
    for j in range(n): #吃药后治好的情况
        if a[j] == '1' and add[eat[i]][j] == '0':
            new_samp.append('1')
        if a[j] == '0' and add[eat[i]][j] == '0':
            new_samp.append('0')
        if add[eat[i]][j] == '1':
            new_samp.append('1')
    init_sam = new_samp

    print(sum(list(map(int,new_samp))))



