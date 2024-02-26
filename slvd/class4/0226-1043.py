#1043 - 거짓말
from collections import deque


tf = [False for i in range(N)]
graph = [[]for i in range(N+1)]
tpeople = []
parties = []

#사람과 파티의 수
N, M = map(int, input().split())

#진실을 아는 사람의 수, 명단
truth  = list(map(int, input().split()))

#truth가 0인 경우
if truth[0] == 0:
    print(M)
else:
    #truth가 여러개인 경우, True로 변경
    for i in range(1,len(truth)-1):
        tpeople.append(truth[i])
        a = truth[i]
        tf[a] = True
    #True와 False
    print("tpeople",tpeople)

    #파티의 수만큼 입력받고 처리하기
    for i in range(M):
        party =list(map(int, input().split()))
        num, people = party[0], party[1:]
        parties.apppend(people)

        #그래프에 넣기
        for i in range(len(people)):
            for j in range(i+1, len(people)):
                graph[people[i]].append(people[j])
                graph[people[j]].append(people[i])
        graph = [list(set(x)) for x in graph]
#bfs
def bfs(x):
    queue = deque(x)
    while queue:
        p = queue.popleft()
        for i in graph[p]:
            if tf[i] == False:
                tf[i] == True
                queue.append(i)

#bfs에 list넣기
                
bfs([x for x in range(1,len(tpeople)))]if tpeople)


    



    while(len(tpeople) != 0):
        member = tpeople.pop()
        for i in range(M):
            if member in party[i]:
                for mem in party[i]:
                    li.append(mem)
                    print(li)





    print(p)
    print(li)