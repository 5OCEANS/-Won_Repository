#2096 - 내려가기
import copy
#N입력받기
N = int(input())

#중간저장용
maxdatas = [0] *3
mindatas = [0] *3

#첫줄 집어넣기
data = list(map(int, input().split()))
dpmin = copy.deepcopy(data)
dpmax = copy.deepcopy(data)

#N-1번 반복
for i in range(N-1):
    data = list(map(int, input().split()))
    maxdatas[0] = max(dpmax[0],dpmax[1]) + data[0]
    maxdatas[1] = max(dpmax) +data[1]
    maxdatas[2] = max(dpmax[1],dpmax[2]) + data[2]
    mindatas[0] = min(dpmin[0],dpmin[1]) + data[0]
    mindatas[1] = min(dpmin)+data[1]
    mindatas[2] = min(dpmin[1],dpmin[2]) + data[2]
    for j in range(3):
        dpmax[j] = maxdatas[j]
        dpmin[j] = mindatas[j]

print(max(dpmax), min(dpmin))



    
