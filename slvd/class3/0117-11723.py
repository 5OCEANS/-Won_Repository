#11723 집합
import sys
input = sys.stdin.readline
time = int(input())
all = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
s = set()
for i in range(time):
    m,n = map(str,input().split())
    n = int(n)
    if m == 'add':
        if n not in s:
            s.add(n)
    elif m == 'check':
        if n in s:
            print(1)
        else:
            print(0)
    elif m == 'remove':
        s.discard(n)
    elif m == 'toggle':
        if n in s:
            s.discard(n)
        else:
            s.add(n)
    elif m == 'all':
        s.clear()
        s.union(all)
    elif m == 'empty':
        s.clear()
    
    
