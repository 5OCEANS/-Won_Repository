#level1 2019 KAKAO BLIND RECRUITMENT 실패율
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
answer = []

def GCD(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def LCM(a,b):
    ans = (a*b) // GCD(a,b)
    return ans


li = [ [0 for i in range(N)],[0 for i in range(N)] ]
for i in range(N):
    li[0][i] = stages.count(i+1)
    for j in range(i+1,N+2):
        li[1][i] += stages.count(j)

lcm = li[1][0]
for i in range(1,N):
    lcm = LCM(lcm,li[1][i])

for i in range(N):
    answer.append(li[0][i] * (lcm // li[1][i]))
result = []
for i in range(N):
    result.append(answer.index(max(answer))+1)
    answer[answer.index(max(answer))] = -1
print(result)

#분수를 바로바로 구하는 방법으로...! 
def solution(N, stages):
    li = []
    st = len(stages)
    for i in range(N):
        cnt = 0
        for j in stages:
            if j == i+1:
                cnt+=1
        if cnt == 0:
            li.append(0)
        else:
            li.append(cnt/st)
            st -= cnt
    result = []
    for i in range(N):
        result.append(li.index(max(li))+1)
        li[li.index(max(li))] = -1
    return result

#level3 DP 정수 삼각형
def solution(triangle):
    N = len(triangle)-1
    for i in range(N):
        k = N-i-1
        for j in range(k+1):

            triangle[k][j] += max(triangle[k+1][j],triangle[k+1][j+1])
    return triangle[0][0]

#level3 거스름돈
def solution(n, money):
    answer = [0 for i in range(n+1)]
    answer[0] = 1

    for j in money:
        for i in range(j,n+1):
            if i >= j:
                answer[i] += answer[i-j]   
    return answer[n]%1000000007

