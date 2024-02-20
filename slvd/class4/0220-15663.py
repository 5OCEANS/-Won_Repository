#15663 - N과 M (9)
N, M = map(int,input().split())
data = list(map(int, input().split()))
data.sort()
s = []
visited = [False] * N
answers = []

def dfs():
    if len(s)==M:
        answer = ' '.join(map(str,s))
        if answer not in answers:
            answers.append(answer)
            print(' '.join(map(str,s)))
        return
    remember = 0
    for i in range(N):
        if visited[i] == False and remember != data[i]:
            s.append(data[i])
            remember = data[i]
            visited[i] = True
            dfs()
            s.pop()
            visited[i] = False
dfs()



