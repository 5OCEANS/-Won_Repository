#3009 네번째 점
xli = []
yli = []
for i in range(3):
    x,y = map(int,input().split())
    xli.append(x)
    yli.append(y)
for i in range(3):
    if xli.count(xli[i]) == 1:
        x4 = xli[i]
    if yli.count(yli[i]) == 1:
        y4 = yli[i]
print(x4, y4)