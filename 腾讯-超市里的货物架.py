n,m = map(int,input().split(' '))
s = input()
c = input()
alphbet = [0]*26
res = 0
tmp = ord('a')
for ss in s:
    alphbet[ord(ss)-tmp] += 1
for cc in c:
    if alphbet[ord(cc)-tmp] >0:
        res+=1
        alphbet[ord(cc)-tmp] = -1
print(res)