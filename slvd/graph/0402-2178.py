#2178 - 미로 탐색
import sys
from collections import deque

n , m = map(int,sys.stdin.readline().split())

map = [list(map(int,' '.join(input().split())))for _ in range(n)]


dx = [0,0,-1,1]
dy = [1,-1,0,0]
def bfs(y,x):
    queue = deque([(y,x)])
    while queue:
        #가장마지막꺼 빼기
        ny,nx = queue.popleft()
        for i in range(4):
            if -1<nx+dx[i]<n and -1<ny+dy[i]<m:
                if map[nx+dx[i]][ny+dy[i]] == 1:
                    map[nx+dx[i]][ny+dy[i]] = map[nx][ny]+1
                    queue.append((ny+dy[i],nx+dx[i]))
                    
bfs(0,0)
print(map[n-1][m-1])
        
