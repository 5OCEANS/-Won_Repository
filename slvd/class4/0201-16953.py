#16953 A->B

a,b = map(int, input().split())

cnt = 1

while(a<b):
    sb = str(b)
    if sb[-1] == '1':
        b= int(sb[:-1])
        cnt+=1
        print(b)
    elif b%2 == 0:
        b//=2
        cnt+=1
        print(b)
    else:
        print(b)
        break
        

if b == a:
    print(cnt)
else:
    print(-1)