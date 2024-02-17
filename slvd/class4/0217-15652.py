#15652 - N과 M(4)

s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()
 
n,m = map(int, input().split())
    
dfs(1)