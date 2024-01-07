#level1 x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    answer.append(x)
    xall = x
    for _ in range(n-1):
        xall += x
        answer.append(xall)
    return answer