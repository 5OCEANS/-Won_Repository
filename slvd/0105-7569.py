#7569 토마토 - bfs 사용 (3차원)
from collections import deque
#M,N,H 입력받기
M, N, H = map(int,input().split())
#토마토 정보 저장하기 M개씩 N번 반복해서 리스트에 넣기
tomato = [[list(map(int, input().split())) for i in range(N)]for _ in range(H)]
#Queue설정
queue = deque([])

#bfs구현
def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx= x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                queue.append([nz,nx,ny])

#정답 저장
result = 0
#가로세로 정보 저장
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0] 
dz = [0,0,0,0,-1,1]

#전체 토마토 반복
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 1:
                #queue에 집어 넣을땐 리스트 형태로 묶어서 좌표넣기
                queue.append([k,i,j])

#bfs실행
bfs()

#답 계산
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 0:
                #익지 않았다면 -1로 끝내기
                print(-1)
                exit(0)
            if tomato[k][i][j] > result:
                result = tomato[k][i][j]

#최소값 출력
print(result-1)