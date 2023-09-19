#ss = input()
#ss= 'aabchgfdecbce'
ss = 'aabhgfdec'
all_combine =set()  #存储所有的连续字串
for i in range(len(ss)):
    all_combine.add(ss[i])
    for j in range(i+1,len(ss)):
        if ord(ss[j]) - ord(ss[j-1]) == 1:
            all_combine.add(ss[i:j+1])
        else:break
#print(all_combine)

nums = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,} #存储以各字母开头的连续字串数目
for s in all_combine:
    nums[s[0]]+=1
#print(nums)

res = 1
for _,num in nums.items():
    res*=num
print(res)
