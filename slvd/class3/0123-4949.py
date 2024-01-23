#4949 균형잡힌 세상
while(True):
    a = input()
    f1 = 0
    f2 = 0
    if a =='.':
        print('Yes')
        break
    else:
        for word in a:
            if word=='(':
                f1+=1
            if word==')':
                f1-=1
            if word=='[':
                f2+=1
            if word==']':
                f2-=1
        if f1==0 and f2==0:
            print('Yes')
        else:
            print('No')