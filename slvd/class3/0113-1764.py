#1764 듣보잡
#list로 풀기
# N, M = map(int, input().split())
# dt = []
# bt = []
# for i in range(N):
#     dt.append(input())
# for i in range(M):
#     name = input()
#     if name in dt:
#         bt.append(name)
# print(len(bt))
# for i in bt:
#     print(i)

#set으로 풀기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dt = set()
bt = set()

for _ in range(N):
    name = input().strip()
    dt.add(name)

for _ in range(M):
    name = input().strip()
    bt.add(name)

result = sorted(list(dt & bt))

print(len(result))
for i in result:
    print(i)
    


    



