#1197 - 최소 스패닝 트리
#0)노드 간선 개수 입력받기
v , e = map(int, input().split())
result = 0

#1)makeSet초기화
parent = [0] * (v+1)
for i in range(1,v+1):
    parent[i] = i

#2)간선 입력받아서 graph에 넣기
graph=[]
for i in range(e):
    a,b,cost = map(int, input().split())
    graph.append((cost,a,b))

#3)cost를 기준으로 정렬하기
graph.sort()

#4)union-find 알고리즘
def find(parent,node):
    #부모와 자식의 값이 같다면 아직 union되기 전이라는 뜻
    if parent[node] == node:
        return node
    #아닐 시 그 부모의 부모노드를 찾아서 가져다주기
    else:
        parent[node] = find(parent,parent[node])
        return parent[node]

def union(parent,a,b):
    #두 노드의 부모 찾아주기
    aroot = find(parent,a)
    broot = find(parent,b)
    #비교해서 작은것으로 통일union시켜주기
    if aroot > broot:
        parent[aroot] = broot
    else:
        parent[broot] = aroot

#5)모든 간선에 대해 사이클이 발생했는지 확인하기

for edge in graph:
    cost,a,b = edge
    #두 노드의 부모가 동일하지 않다면, union대상
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        #가중치 값 추가
        result += cost

print(result)