#15650 - N과 M(2)

N,M = map(int, input().split())
s = []
def dfs(start):
    lenli = len(s)
    if lenli == M:
        print(''.join(map(str,s)))
        return
    for i in range(start,N+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(1)
 