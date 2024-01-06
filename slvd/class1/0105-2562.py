#2562최댓값
answer = 0
cnt = 0
for i in range(9):
    N = int(input())

    if answer <= N:
        answer = N
        cnt = i
print(answer)
print(cnt+1)




