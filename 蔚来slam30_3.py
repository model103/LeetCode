n = int(input())
board = list(map(int, input().split(' ')))
board.sort()
l = 0
while l < board[n - l - 1]:
    l += 1
print(l)


