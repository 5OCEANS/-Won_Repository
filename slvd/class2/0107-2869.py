#반복문 사용 -> 시간초과 -> 바로 계산해야함!
A, B, V = map(int, input().split())
day = 0
snail = 0

while snail < V:
    day += 1
    snail += A
    if snail >= V:
        break
    snail -= B

#반복문 사용하지 않는 버전
import math
A, B, V = map(int, input().split())
day = (V-B) / (A-B)

print(math.ceil(day))




