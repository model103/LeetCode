class Solution:
    def rotApple(self , grid) -> int:
        # write code here
        self.n = len(grid)
        self.m = len(grid[0])
        res = 0
        self.freshapple = 0
        next_expand = []
        for row in range(self.n):
            for col in range(self.m):
                if grid[row][col] == 1: self.freshapple+=1
                elif grid[row][col]==2: next_expand.append([row,col])
        while next_expand:
            if self.freshapple==0:break
            new_to_expand = []
            for p in next_expand:
                self.ex_out(grid,p[0],p[1],new_to_expand)

            next_expand = new_to_expand
            res+=1
        if self.freshapple>0:
            return -1
        return res

    def ex_out(self,grid,row,col,new_to_expand):
        if row >0:
            if grid[row-1][col] == 1:
                grid[row-1][col] = 2
                new_to_expand.append([row-1,col])
                self.freshapple-=1
        if row <self.n-1:
            if grid[row +1][col] == 1:
                grid[row + 1][col] = 2
                new_to_expand.append([row + 1, col])
                self.freshapple -= 1
        if col>0:
            if grid[row][col-1] == 1:
                grid[row][col-1] = 2
                new_to_expand.append([row, col-1])
                self.freshapple -= 1
        if col <self.m-1:
            if grid[row][col+1] == 1:
                grid[row][col+1] = 2
                new_to_expand.append([row, col+1])
                self.freshapple -= 1

a = Solution()
print(a.rotApple([[2,1,1],[1,0,1],[1,1,1]]))