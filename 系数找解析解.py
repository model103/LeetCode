
x = list(map(int, input().split(' ')))

flag = [True] * 6
l = len(x)
for i in range(0, l):

    if x[0] != x[i]:
        flag[0] = False
    if i < l-1:
        if x[1] / x[0] != x[i + 1] / x[i]:
            flag[1] = False
    if i < l-2:
        if (x[2] - x[0]) != (x[i + 2] - x[i]):
            flag[2] = False
        if (x[1] * x[0])!=0:
            if (x[2] * x[1]) / (x[1] * x[0]) != (x[i + 2] * x[i + 1]) / (x[i + 1] * x[i]):
                flag[3] = False
        else: flag[3] = False
        if (x[0] + x[2] - 2 * x[1])!= 0:
            k = (x[0] * x[2] - x[1] ** 2) / (x[0] + x[2] - 2 * x[1])
            if (x[1]-k)/(x[0]-k) != (x[i+1]-k)/(x[0]-k):
                flag[4] = False
        else: flag[4] = False

    if i < l-3:
        if (x[1] ** 2 - x[0] * x[2]) != 0 and  (x[2] ** 2 - x[1] * x[3]) / (x[0] * x[2] - x[1] ** 2) != 0:
            if (x[1] * x[2] - x[0] * x[3]) / (x[1] ** 2 - x[0] * x[2]) != (x[i + 1] * x[i + 2] - x[i + 0] * x[i + 3]) / (
                    x[i + 1] ** 2 - x[i + 0] * x[i + 2]) and (x[2] ** 2 - x[1] * x[3]) / (x[0] * x[2] - x[1] ** 2) !=(x[i+2] ** 2 - x[i+1] * x[i+3]) / (x[i+0] * x[i+2] - x[i+1] ** 2):
                flag[5] = False
        else:flag[5] = False

op = -1
for i in range(6):
    if flag[i] ==True:
        op = i
        break
if op == -1:
    print('wrong')

else:
    if op == 0:
        print(x[0])
    if op == 1:
        print(x[-1]*x[1]/x[0])
    if op == 2:
        print(x[-1]*x[2]/x[0])
    if op ==3:


