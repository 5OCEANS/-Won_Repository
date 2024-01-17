#level3 사칙연산
arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]
def solution(arr):
    #딕셔너리 만들기
    d = {}
    for i in range(0,len(arr)-1,2):
        d[int(arr[i])] = arr[i+1]
    #print(d)
    
    intarr = [int(i) for i in arr if i.isdigit()]
    #print(intarr)
    
    intcount = len(intarr)
    dp = [[0 for i in range(intcount)]for i in range(intcount)]
    
    #1칸 채우기
    for i in range(intcount):
        dp[0][i] = intarr[i]
    
    for i in range(1,intcount):
        for j in range(i,intcount):
            if d.get(intarr[j-1]) == '+':
                a = dp[i-1][j-1]+dp[0][j]
                #print(dp[i-1][j-1],d.get(intarr[j-i]),"+",dp[0][j])
            else:
                a = dp[i-1][j-1]-dp[0][j]
                #print(dp[i-1][j-1],d.get(j-i),"-",dp[0][j])
            if d.get(intarr[j-i]) == '+':
                b = dp[0][j-i]+dp[i-1][j]
                #print(dp[0][j-i],d.get(j-i),"+",dp[i-1][j])
            else:
                b = dp[0][j-i]-dp[i-1][j]
                #print(dp[0][j-i],d.get(j-i),"-",dp[i-1][j])
            #print(a,b)
            dp[i][j] = max(a,b)
    #print(dp)
    #print(dp[intcount-1][intcount-1])
    return dp[intcount-1][intcount-1]

solution(arr)