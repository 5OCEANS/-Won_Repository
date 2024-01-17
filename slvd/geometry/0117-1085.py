#1085 직사각형에서 탈출
x,y,w,h = map(int,input().split())

if 2*x>w:
    a = w-x
else:
    a = x
if 2*y>h:
    b = h-y
else:
    b = y
print(min(a,b))