#15650 - N과 M(2)

n,m = list(map(int,input().split()))
lista = []
def dfs(start):
    lenli = len(lista)
    if lenli == m:
        print(' '.join(map(str,lista)))
        return
    
    for i in range(start,n+1):
        if i not in lista:
            lista.append(i)
            #dfs를 시작점 갱신해서 실행
            dfs(i+1)
            lista.pop()
dfs(1)
 