#9012 괄호
N = int(input())
for i in range(N):
    stack = []
    li = list(input())
    for j in li :
        if len(stack)>0:
            if stack[-1] == '(' and j == ')':
                stack.pop()
            else:
                stack.append(j)
        else:
           stack.append(j) 
    if len(stack)==0:
        print("YES")
    else:
        print("NO")
    