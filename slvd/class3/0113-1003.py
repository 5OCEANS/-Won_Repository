#1003 피보나치 함수

T = int(input())
for i in range(T):
    N = int(input())
    fib = [[0 for i in range(2)]for i in range(N+1)]
    

    fib[0][0] = 1
    if(N > 0):
        fib[1][1] = 1
    if(N > 1):
        for i in range(2,N+1):
            fib[i][0] = fib[i-1][0] + fib[i-2][0]
            fib[i][1] = fib[i-1][1] + fib[i-2][1]
    print(fib[N][0],fib[N][1],end=" ")

    
