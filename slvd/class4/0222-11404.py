#11404 - 플로이드

#도시의 개수 N입력받기
N = int(input())
#버스의 개수 M입력받기
M = int(input())

#플로이드 2차원 배열 만들기
dp = [[ int(1e9) for i in range(N)] for i in range(N)]

#0초기화
for i in range(N):
    dp[i][i] = 0

#버스의 정보 입력받기
for i in range(M):
    a,b,c = map(int, input().split())
    dp[a-1][b-1] = min(dp[a-1][b-1],c)

#N개의 도시를 거쳐가는 방법으로 업데이트 진행
for k in range(N):
    #2차원 배열 탐색
    for i in range(N):
        for j in range(i):
            if k == i or k == j:
                continue
            else:
                dp[i][j] = min(dp[i][j],dp[i][k]+ dp[k][j])
                dp[j][i] = min(dp[j][i],dp[j][k]+ dp[k][i])

for i in range(N):
    for j in range(N):
        if dp[i][j] == int(1e9):
            print("0",  end=" ")
        else:
            print(dp[i][j],end=' ')
    print()
    
    
