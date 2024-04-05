#12100 - 2048(easy)

#1)N입력받기
n = int(input())

#3)board 생성하고 초기값 입력받기
board = [list(map(int,' '.join(input().split())))for _ in range(n)]
print(board)