#15663 - N과 M (12)
N, M = map(int,input().split())
data = list(map(int, input().split()))
data.sort()
s = []
visited = [False] * N
answers = []

def dfs(start):
    if len(s)==M:
        answer = ' '.join(map(str,s))
        if answer not in answers:
            answers.append(answer)
            print(' '.join(map(str,s)))
        return
    for i in range(start,N):
        s.append(data[i])
        dfs(i)
        s.pop()
dfs(0)