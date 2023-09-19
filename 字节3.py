def min_operations_to_good_array(n, arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    distinct_nums = len(freq)
    max_freq = max(freq.values())
    min_operations = min(n - max_freq, distinct_nums - 1)

    return min_operations

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Calculate and print the result
flag = True
for i in arr:
    if i!=arr[0]:
        flag = False
        break
if flag:
    print(1)
else:
    result = min_operations_to_good_array(n, arr)
    print(result)
