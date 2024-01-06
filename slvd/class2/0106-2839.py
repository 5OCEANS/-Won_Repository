#2839 설탕배달 - Dp로 풀기

N = int(input())

#DP위한 배열 생성(1개 더 많이..!)
list = [0] * (N+1)

#3과 5초기화
list[3] = 1
list[5] = 1

#i번째 list값은 i+1
for i in range(N+1):
    if i < 6:
        continue
    elif list[i-5] != 0:
        list[i] = list[i-5] + 1
    elif list[i-3] != 0:
        list[i] = list[i-3] + 1
print(list)
print(list[N])

