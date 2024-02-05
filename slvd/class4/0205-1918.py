#1918 - 후위 표기식

a = list(input())

stack = []
answer =""

for i in a:
    if i == '(':
        stack.append(i)
    elif i == ')':
        while stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
    elif ord(i)>=65 and ord(i)<=90:
        answer += i
    #*, /
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        stack.append(i)
    #+,-
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.append(i)
while len(stack) != 0:
    answer += stack.pop()
print(answer)