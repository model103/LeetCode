from 链表 import creat_linklist

def nextLargenode(head):
    #对于某个节点i不是找后面比他大的点，
    # 而是对于某节点i找前面的比他小的递减序列，这些递减序列的下一个更大节点均为该节点i
    ans = []
    stack = [] #存储没找到下个更大节点的递减序列,(值，在ans中对应的位置)
    idx = 0  #存储链表的idx
    cur = head
    while cur:
        ans.append(0)  #先当做没有下个更大节点
        while stack and cur.val > stack[-1][0]:
            ans[stack[-1][1]] = cur.val
            stack.pop()  #把比cur.val大的都pop了
        stack.append((cur.val, idx)) #再把cur.val压进去，这样保证了stack的递减序列
        idx += 1
        cur = cur.next
    return ans

data = [2,7,4,3,5]
head = creat_linklist(data)
print(nextLargenode(head))

