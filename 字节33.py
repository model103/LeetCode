def cal(nums):
    nums.sort()
    return sum(abs(num - nums[len(nums) // 2]) for num in nums)

n = int(input())
arr = list(map(int,input().split(' ')))
min_ops = float('inf')
flag = True
for i in range(n):
    min_ops = min(min_ops,cal(arr[0:i] + arr[i+1:]))
    if arr[i] != flag:
        flag = False

if flag:
    print(1)
else:print(min_ops)
