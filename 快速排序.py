def quick_sort1(data:list):
    #时间复杂度O(nlog2n)，空间复杂度O(nlog2n)
    if len(data)<2:
        return data
    th = data[0]
    #data.remove(th) #remove按值查找，删除第一个匹配的元素 #del,pop按索引查找，删除索引对应元素
    left, right = [], []
    for num in data[1:]:
        if num <= th:
            left.append(num)
        else:
            right.append(num)
    return quick_sort1(left) + [th] + quick_sort1(right)

def quick_sort2(data:list):
    #原地排序版，时间复杂度O(nlog2n)，空间复杂度O(1)
    if len(data) < 2:
        return data
    i, j = 0, len(data)-1  #data[0]为th
    flag = False #F表示j往前遍历，T表示i往后遍历
    while(i < j):
        if flag == False:  #j向前便利
            if data[j] < data[i]:
                data[i], data[j] = data[j], data[i]#交换后th是data[j]
                flag = True
            else:
                j -= 1
        else:
            if data[i] >= data[j]:
                data[i], data[j] = data[j], data[i] #交换后th是data[i]
                flag = False
            else:
                i += 1
    return quick_sort2(data[:i]) + [data[i]] + quick_sort2(data[i+1:])

def quick_sort3(data:list):
    #quick_sort2的优雅版本，也是最常用的版本
    if len(data) < 2:
        return data
    th = data[0]
    i, j = 0, len(data)-1
    while(i<j):
        while data[j] >= th and i < j:
            j -= 1
        data[i] = data[j]
        while data[i] < th and i < j:
            i += 1
        data[j] = data[i]
    data[i] = th
    return quick_sort3(data[:i]) + [th] + quick_sort3(data[i+1:])

data = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
print(data)
print(quick_sort1(data))
print(quick_sort2(data))
print(quick_sort3(data))

