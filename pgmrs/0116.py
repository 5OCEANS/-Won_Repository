#level3 사칙연산
arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]
def solution(arr):
    #딕셔너리 만들기
    d = {}
    for i in range(0,len(arr)-1,2):
        d[arr[i]] = arr[i+1]
    
    intarr = []
    
    intcount = len(arr)//2+1
    dp = [[0 for i in range(intcount)]for i in range(intcount)]
    
    #1칸 채우기
    for i in range(len(arr)):
        dp[0][i]
        
    

solution(arr)