#一组list，表示每个怪兽的血量，每次让两只怪兽决斗，一比一换血，直到只剩下一只或0只怪兽，请问最后的怪兽血量最低是多少？以及对决的次数和对应哪两只怪兽对决
#思路，01背包问题，背包容量为总血池的一半，找出最接近总血池的一半的怪兽组合A，剩下的为组合B，一次让A中的和B中的怪兽对决。

n = int(input())
hp_ = list(map(int, input().split(' ')))
all_hp = sum(hp_)
idx = list(range(n + 1))[1:]
hp = list(list(h) for h in zip(hp_, idx))  # 记录排序前的下标
hp.sort(key=lambda x: x[0])

# 分两组，使得两组的总血池差值最低
l = 0  # 左边组的最后一个元素位置
l_hp = 0
min_diff = abs((all_hp - l_hp) - l_hp)
for i in range(n):
    l_hp += hp[i][0]
    diff = abs((all_hp - l_hp) - l_hp)
    if diff < min_diff:
        min_diff = diff
        l = i
    else:
        break
# 输出
print(min_diff)
times = 0
fight = []
sur_nums = n  # 存活的怪物数
l_idx, r_idx = 0, l + 1  # 左右两组中当前决斗的怪物idx
while sur_nums > 1:
    fight.append([hp[l_idx][1], hp[r_idx][1]])
    if hp[l_idx][0] < hp[r_idx][0]:
        hp[r_idx][0] -= hp[l_idx][0]
        hp[l_idx][0] = 0
        l_idx += 1
        sur_nums -= 1
    elif hp[l_idx][0] > hp[r_idx][0]:
        hp[l_idx][0] -= hp[r_idx][0]
        hp[r_idx][0] = 0
        r_idx += 1
        sur_nums -= 1
    elif hp[l_idx][0] == hp[r_idx][0]:
        hp[l_idx][0] = hp[r_idx][0] = 0
        l_idx += 1
        r_idx += 1
        sur_nums -= 2
    times+=1
print(times)
for f in fight:
    print(f[0], f[1])
