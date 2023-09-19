class Solution:
    def reverse(self , x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x = abs(x)
        res = 0
        while x:
            if flag == 1 and res > ((1 << 31) -1 - x % 10) /10:
                return 0
            if flag == -1 and res >((1 << 31 )- x % 10) /10:
                return 0
            res = res *10 +x %10
            x = x//10
        return flag * res
