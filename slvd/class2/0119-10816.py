#10816 숫자카드2
from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

dic = {}

for i in card:
    if i in hash:
        dic[i] += 1
    else:
        dic[i] = 1

for j in test:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')