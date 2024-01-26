#11659 - 구간합구하기4
import sys
input = sys.stdin.readline
num = 0 
sum = [0] 

#입력받기
m, n = map(int, input().split())
x = list(map(int, input().split()))
 
for i in x:
    num += i
    sum.append(num)
 
for i in range(n):
    a, b = map(int, input().split())
    print(sum[b] - sum[a-1])
