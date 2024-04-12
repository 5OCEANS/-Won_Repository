#20162 - 간식파티

#1)N 입력받기
n = int(input())
#2)간식 만족도 입력받기
calender = [ int(input()) for _ in range(n)]
#3)평점의 합 리스트 만들기
star = [ 0 for _ in range(n)]
#4)첫값초기화
star[0] = calender[0]
#5)N번반복하면서 dp수행
for i in range(1,n):
    #현재 간식 만족도
    favor = calender[i]
    plus = 0
    for j in range(i):
        #만족도가 현재보다 작은 것들 중에 평점의 합이 제일 높은 것 선택
        if (calender[j] < favor) and (star[j] > plus):
            plus = star[j]
    #평점의 합 갱신
    star[i] = favor + plus
#6)최댓값 출력
print(max(star))
            


