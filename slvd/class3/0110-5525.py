N = int(input())
M = int(input())
li = list(input())
cnt = 0

for i in range(M):
    if li[i] == 'I' and i < M-2*N:
        bool = True
        for j in range(N):
            print(li[i],li[i+2*j+1],li[i+2*j+2])
            if li[i+2*j+1] == 'O' and li[i+2*j+2] == 'I':
                continue
            else:
                bool = False
        if bool == True:
            cnt+=1
        
print(cnt)
              
        
