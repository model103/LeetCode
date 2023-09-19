#k = int(input())

def count(k):
    if k == 1:
        return 1
    else:
        tmp1 = (k - 2) // 4
        tmp2 = (k - 2) % 4
        res = tmp1 * 2 + tmp2
        return res

for k in range(1,20):
    print(count(k))

