n = int(input())
ss = input().split(' ')
arr = []
if ss[0].isdigit():
    arr.append(int(ss[0]))
arr+=map(int,ss[1:-1])
if ss[-1].isdigit():
    arr.append(int(ss[-1]))
#arr = list(map(int, input().split(' ')))
arr_sum =sum(arr)
cap = arr_sum//2



def zero_one_package(cost,value,cap):
    dp=[0]*(cap+1)
    for i in range(0,n):
        for j in range(cap,0,-1):
            if cost[i] <=j:
                dp[j] =max(dp[j],dp[j-cost[i]] + value[i])
    return dp[-1]

res = zero_one_package(arr,arr,cap)
if res != arr_sum/2:
    print('false')
else:print('true')
