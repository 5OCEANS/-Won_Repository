#2630 - 색종이 만들기
N = int(input())
lista = []
cnt = [0,0]

def dnc(startx,starty,line):
    if line < 1:
        cnt[color]+=1
        return
    else:
        picx = startx
        picy = starty
        color = lista[picx+i][picy+j]
        for i in range(line):
            for j in range(line):
                if color != lista[picx+i][picy+j]:
                    dnc(startx,starty,line//2)
                    dnc(startx+line//2,starty,line//2)
                    dnc(startx,starty+line//2,line//2)
                    dnc(startx+line//2,starty+line//2,line//2)
                    return
        cnt[color]+=1

for k in range(N):
    A = list(map(int, input().split()))
    lista.append(A)
dnc(0,0,N)
print(cnt[0],cnt[1])