#15657 - N과 M (8)
N,M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
s = []

def dfs(start):
    lenli = len(s)
    if lenli == M:
        print(' '.join(map(str,s)))
        return
    for i in range(start,N):
        s.append(data[i])
        dfs(i)
        s.pop()
dfs(0)