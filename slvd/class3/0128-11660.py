#11660 - 구간합구하기5

import sys
input = sys.stdin.readline
#입력받기
n, m = map(int, input().split())

sum = [0]
#입력받고 잘라서 넣기
for i in range(n):
    a = list(map(int, input().split()))
    sum.append(a)

#dp 
dp = [[0]*(n+1) for i in range(n+1)]

#반복하면서 dp배열 채우기
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + sum[i-1][j-1]

#xy값 입력받기
for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())

    #정답저장
    answer = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    print(answer)