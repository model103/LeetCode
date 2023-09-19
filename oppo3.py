n = int(input())
s = ''
for i in range(n // 3):
    s += 'opp'
oppo = 'oppo'
s += oppo[:n % 3]
print(s)
