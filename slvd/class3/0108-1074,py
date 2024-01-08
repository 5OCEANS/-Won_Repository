#1074 Z

#완전탐색D&C -> 런타임에러.......
# N, r, c = map(int, input().split())
# width = N**2

# list = [[0 for _ in range(width)] for _ in range(width)]

# def divide(a,b,n):
#     global cnt
#     if n == 2:
#         list[a][b] = cnt
#         cnt += 1
#         list[a][b+1] = cnt
#         cnt += 1
#         list[a+1][b] = cnt
#         cnt += 1
#         list[a+1][b+1] = cnt
#         cnt += 1
#     else:
#         divide(a,b,n//2)
#         divide(a,b+n//2,n//2)
#         divide(a+n//2,b,n//2)
#         divide(a+n//2,b+n//2,n//2)

# cnt = 0
# divide(0,0,width)
# print(list[r][c])

#입력
N, r, c = map(int, input().split())
width = 2**N
def divide(a,b,n):
    global cnt
    if a>r or a+n<=r or b>c or b+n<=c:
        cnt += n**2
        return
    
    if n > 2:
        n//=2
        divide(a,b,n)
        divide(a,b+n,n)
        divide(a+n,b,n)
        divide(a+n,b+n,n)
    else:
        if a == r and b == c:
            print(cnt)
        elif a == r and b+1 == c:
            print(cnt+1)
        elif a+1 == r and b == c:
            print(cnt+2)
        else:
            print(cnt+3)
        sys.exit
       

cnt = 0
divide(0,0,width)
        






