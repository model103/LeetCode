s = input()
n = len(s)
i = 0
k = j = (n + 1) // 2
while i <= n // 2 and j < n and k < n:
    if s[i] == s[j]:
        j += 1
        i += 1
    else:
        i = 0
        k += 1
        j = k
print(j - k)
