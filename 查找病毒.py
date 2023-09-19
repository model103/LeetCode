#直接暴力法模板匹配

t = int(input())

def is_virus(star_i,star_j,end_i,end_j,arr_n,arr_m,ratio):#图像金字塔提速,ratio为下采样倍率
    for i in range(star_i,end_i,ratio):
        for j in range(star_j,end_j,ratio):
            flag = True
            for k in range(0,m,ratio):
                for l in range(0,m,ratio):
                    if arr_m[k][l] != arr_n[i+k][j+l]:
                        flag = False
                        break
                if flag == False: break
            if flag == True:
                is_virus(i,j,i+ratio,j+ratio,arr_n,arr_m,ratio//2)







for i in range(t):
    arr_n = []
    arr_m = []
    n,m = map(int, input())
    for _ in range(n):
        arr_n.append(list(map(int, input())))
    for __ in range(m):
        arr_m.append(list(map(int, input())))

    print(is_virus(n,m,arr_n,arr_m,(m**0.5)%1)) #




