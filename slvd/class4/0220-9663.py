n = int(input())
#table=[]
# def correct(r,c):
#     if len(table)>0:
#         for k in range(len(table)):
#             if table[k][0] == r or table[k][1] == c:
#                 return False
#             if abs(table[k][0] - r) == abs(table[k][1]-c):
#                 return False
#     return True
# def bound(r,c):
#     if (r>=0 and r<N) and (c>=0 and c<N) :
#         return True
#     else:
#         return False
# cnt = 0
# r,c = 0,0
# while(True):
#     if correct(r,c) == True and bound(r,c)== True :
#         table.append([r,c])
#         r += 1
#         c = 0
#     elif c >= N:
#         if len(table) == N:
#             cnt+=1
#             last = table.pop()
#             r = last[0]
#             c = last[1]+1
#         elif len(table) == 0:
#             break
#         else:
#             last = table.pop()
#             r = last[0]
#             c = last[1]+1
#     else:
#         c += 1
# print(cnt)

check_row = [0 for i in range(n)]
check_leftcross = [0 for i in range(n*2)]
check_rightcross = [0 for i in range(n*2)]
ret = 0

def backtracking(cur):
    if cur==n:
        global ret
        ret += 1
        return 0
    for i in range(n):
        if check_row[i] or check_leftcross[n+cur-i] or check_rightcross[cur+i]:
            continue
        else:
            check_row[i] = 1
            check_leftcross[n+cur-i] = 1
            check_rightcross[cur+i] = 1
            backtracking(cur+1)
            check_row[i] = 0
            check_leftcross[n+cur-i] = 0
            check_rightcross[cur+i] = 0


for i in range(n//2):
    check_row[i] = 1
    check_leftcross[n-i] = 1
    check_rightcross[i] = 1
    backtracking(1)
    check_row[i] = 0
    check_leftcross[n-i] = 0
    check_rightcross[i] = 0
ret = ret*2

if n%2: #홀수일경우
    i=n//2
    check_row[i] = 1
    check_leftcross[n-i] = 1
    check_rightcross[i] = 1
    backtracking(1)
    check_row[i] = 0
    check_leftcross[n-i] = 0
    check_rightcross[i] = 0

print(ret)


