#9251 - LCS

#두 수열 입력받기
first = list(input())
second = list(input())

#dp배열 생성
dp = [[ 0 for i in range(len(second)+1)]for i in range(len(first)+1)]

#for문 돌면서 찾기
for i in range(len(first)):
    for j in range(len(second)):
        if first[i] == second[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])

print(dp[len(first)][len(second)])