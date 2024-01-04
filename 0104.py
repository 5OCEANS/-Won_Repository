#7576 토마토 - bfs 사용
from collections import deque
#M,N입력받기
M, N = map(int,input().split())
#토마토 정보 저장하기 M개씩 N번 반복해서 리스트에 넣기
tomato = [list(map(int, input().split())) for i in range(N)]
#Queue설정
queue = deque([])

#bfs구현
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx= x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx,ny])

#정답 저장
result = 0
#가로세로 정보 저장
dx = [-1,1,0,0]
dy = [0,0,-1,1] 

#전체 토마토 반복
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            #queue에 집어 넣을땐 리스트 형태로 묶어서 좌표넣기
            queue.append([i,j])

#bfs실행
bfs()

#답 계산
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            #익지 않았다면 -1로 끝내기
            print(-1)
            exit(0)
        if tomato[i][j] > result:
            result = tomato[i][j]

#최소값 출력
print(result-1)