s = input()
t = input()
flag = 0  # 记录s中原本就是顺序排列的字母个数
t_idx = 0
for i in range(len(s)):
    if s[i] == t[t_idx]:
        flag += 1
        t_idx += 1
print(len(s) - t_idx)
