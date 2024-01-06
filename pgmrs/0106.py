#level1 약수의 합
def solution(n):
    answer = 0

    for i in range(1,n+1):
        if n % i == 0:
            answer += i 
    return answer

#level1 평균 구하기
def solution(arr):
    answer = 0
    for i in range(len(arr)):
        answer += arr[i]
    answer = answer / len(arr)
    return answer

#level1 짝수와 홀수
def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer

#level1 나머지가 1이 되는 수 찾기
def solution(n):
    for i in range(1,n):
        if n % i == 1:
            return i