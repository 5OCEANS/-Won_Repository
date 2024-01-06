N = int(input())

slist = []
for i in range(N):
    a,b = input().split()
    slist.append([int(a),b])

slist.sort(key = lambda a: a[0])

for i in range(N):
    print(slist[i][0], slist[i][1])