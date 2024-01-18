#나는야 포켓몬 마스터 이다솜
#import sys
#input = sys.stdin.readline

N,M =map(int, input().split())
dic1 = {}
dic2 = {}
for i in range(1,N+1):
    name = input()
    dic1[i] = name
    dic2[name] = i
for i in range(M):
    quest = input()
    if quest.isdigit():
        quest = int(quest)
        print(dic1[quest])
    else:
        print(dic2[quest])

        
        

