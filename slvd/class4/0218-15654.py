#15654 - N과 M (5)
n, m = map(int, input().split())
data = list(map(int , input().split()))
data.sort()
visited = [False] * n
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(n):
        if not visited[i]:
            s.append(data[i])
            visited[i] = True
            dfs()
            visited[i] = False
            s.pop()

dfs()
