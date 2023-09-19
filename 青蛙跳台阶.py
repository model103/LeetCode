class Solution:
    def combination(self,m,n):
        numer = 1
        demon = 1
        if m == 0:
            return 0
        for i in range(m):
            numer = numer * n
            n -= 1
            demon = demon * m
            m -= 1
        return int(numer/demon)
    def numWays(self, n: int) -> int:
        num = 0
        for i in range(n//2):
            num += self.combination(i+1,i+1 + (n-2*(i+1)))
        return (num + 1) % (10**9 +7)

a = Solution()

print(a.numWays(44))


#其实可转换成斐波那契数列
