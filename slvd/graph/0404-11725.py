# #11725 - 트리의 부모 찾기

# #노드의 개수 입력받기
# n = int(input())

# parent = [100001] * (n+1)

# parent[1] = 1
# graph =[]

# #반복해서 받고 그래프에 넣기
# for i in range(n-1):
#     a,b = map(int,input().split())
#     graph.append((b,a))

# for node in graph:
#     a,b = node
#     roota = parent[a]
#     rootb = parent[b]

#     if roota > rootb:
#         parent[a] = b
#     elif roota < rootb:
#         parent[b] = a

# for i in range(2,n+1):
#     print(parent[i])

#11725 - 트리의 부모 찾기

#노드의 개수 입력받기
n = int(input())

parent = [100001] * (n+1)
parent[1] = 1

#반복해서 받고 그래프에 넣기
for i in range(n-1):
    a,b = map(int,input().split())
    roota = parent[a]
    rootb = parent[b]

    if parent[a] > parent[b]:
        parent[a] = b
    elif parent[a] < parent[b]:
        parent[b] = a

for i in range(2,n+1):
    print(parent[i])