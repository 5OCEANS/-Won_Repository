#1629 - 곱셈
def dnc(a, b, c):
    #1이면 그대로의 값 출력
    if b == 1:
        return a % c
    #아니면 2로 나눈값 함수에 넣기
    temp = dnc(a, b // 2, c)

    #나머지의 경우에 따라 다른 계산
    if b % 2 == 1:
        return ((temp * temp) % c) * a % c
    else:
        return (temp * temp) % c

#abc입력받기
a, b, c = map(int, input().split())
#계산
answer = dnc(a, b, c)
#출력
print(answer)