#12100 - 2048(easy)

#1)N입력받기
n = int(input())

#3)board 생성하고 초기값 입력받기
board = [list(map(int,' '.join(input().split())))for _ in range(n)]
print(board)

dy = [0,0,-1,1]
dx = [-1,1,0,0]

#4)탐색 구현
def do(line):
    lenline = len(line)
    for i in range(lenline):

        #처음이 0으로 시작하지 않을 경우에 02202
        if i == 0 and line[0] == 0:
            for i in range(1,lenline):
                if line[i] != 0:
                    line[0] = line[i]
                    line[i] = 0
                    break
        
        #처음이 0이 아닌 상태에서 시작20202
        

        
            

        
