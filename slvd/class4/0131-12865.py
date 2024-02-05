#12865 평범한 배낭
n, k = map(int, input().split())
items = []
for i in range(n):
    a,b = map(int, input().split())
    items.append([a,b])
dp =[[ 0 for i in range(k+1)]for i in range(n+1)]

for i in range(1, n+1):
    for j in range(k+1):
        itemk = items[i-1][0]
        itemv = items[i-1][1]
        if j>=itemk:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-itemk]+itemv)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])
        
    