#11399 ATM

N = int(input())
timelist = list(map(int,input().split()))
timelist.sort()
answer = 0
for i in range(N+1):
    answer += sum(timelist[0:i])
print(answer)