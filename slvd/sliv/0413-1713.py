#1713 - 후보추천하기
#1)사진틀의 개수 입력
n = int(input())
#2)전체학생의 총 추천횟수
m = int(input())
#3)사진틀, 추천횟수 만들기
photo = [0 for _ in range(n)]
like = [0 for _ in range(n)]
latest = [0 for _ in range(n)]
late = 0
#4)후보 입력받기
can = list(map(int, input().split()))
print(can)
for i in range(m):
    late+=1
    #이미 등록되어있는 경우
    if can[i] in photo:
        #해당 후보에게 좋아요 추가
        like[photo.index(can[i])] += 1
    else:
        #사진틀이 비어있는 경우 등록시키기
        if 0 in photo:
            now = photo.index(0)
        else:
            #추천 받은 횟수가 가장 적은 후보가 여러명일때
            if like.count(min(like)) > 1:
                #게시된지 오래된 사진을 삭제
                now = latest.index(min(latest))
            else:
                #추천받은 횟수가 가장 적은 후보 몰아내기
                now = like.index(min(like))
        #값변경하기
        like[now] = 1
        photo[now] = can[i]
        latest[now] = late

photo.sort()
for c in photo:
    print(c,end=" ")

            

        



