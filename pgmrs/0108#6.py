#level1 2024 KAKAO WINTERINTERNSHIP 가장 많이 받은 선물

def solution(friends, gifts):
    #return용
    answer = 0
    #딕셔너리 생성
    dict = {}
    #친구의 수
    fr = len(friends)
    #정답 계산용 배열
    result = [0 for i in range(fr)]

    #친구:번호 딕셔너리 생성
    for i in range(fr):
        dict[friends[i]] = i
    #딕셔너리 상태 확인
    #print(dict)

    #gift처리용 2차원 배열 생성 -> 0으로 초기화
    giftlist = [[0 for i in range(fr)] for i in range(fr)]

    #선물지수 처리용 3 * fr 배열 생성 [준,받은,선물지수]
    giftscore =[ [0 for i in range(3)]for i in range(fr)]

    #gifts기반 giftlist내용 채우기
    for i in range(len(gifts)):
        #공백 기준 문자열 분할
        giftfr = gifts[i].split()
        #dict[giftfr[0]]:준 dict[giftfr[1]]:받은
        give = dict[giftfr[0]]
        get = dict[giftfr[1]]
        #선물 개수 늘리기
        giftlist[give][get] += 1
    
    #giftlist기반 giftscore(선물지수) 내용채우기
    for i in range(fr):
        # i 가 준 선물 계산
        for j in range(fr):
            #giftscore[i][0] = i가 줌
            giftscore[i][0] += giftlist[i][j]
            #giftscore[i][1] = i가 받음
            giftscore[i][1] += giftlist[j][i]
        #giftscore[i][2] = 줌 - 받음 (선물지수)
        giftscore[i][2] = giftscore[i][0] - giftscore[i][1]
    
    #전체 계산
    #친구들끼리 한번씩 비교(리그 형식)
    for i in range(fr):
        for j in range(i,fr):
            #선물을 주고받은 기록이 없는 경우, 선물을 주고받은 수가 같은 경우
            if (giftlist[i][j] == 0 and giftlist[j][i] == 0) or (giftlist[i][j] == giftlist[j][i]):
                #선물지수 지수 비교
                #선물지수도 동일 한 경우
                #if giftscore[i][2] == giftscore[j][2]:
                    #다음달에 선물을 주고받지 않는다 - 굳이 작성 안해도 될듯
                    #continue 
                #i>j의 경우
                if giftscore[i][2] > giftscore[j][2]:
                    #i가 j에게 선물을 하나 받는다. -> i의 점수 ++
                    result[i]+=1
                #i
                elif giftscore[i][2] < giftscore[j][2]:
                    result[j]+=1
            #선물을 주고받은 기록이 있는 경우
            elif giftlist[i][j]>giftlist[j][i]:
                result[i]+=1
            elif giftlist[i][j]<giftlist[j][i]:
                result[j]+=1
    #제일 큰 값 찾기
    answer = max(result)
    #print(max(result))
    return answer


#level1 음양더하기
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    
    return answer

#level1 정수 내림차순으로 배치하기
def solution(n):
    #list에 하나씩
    li = list(str(int(n)))
    li.sort(reverse=True)
    answer = ("".join(li))
    return int(answer)

#level1 문자열 정수로 바꾸기
def solution(s):
    li = list(s)
    if li[0] == '-' :
        del li[0]
        answer = 0 - int("".join(li))
    else:
        answer = int("".join(li))
    return answer

#level1 자릿수 더하기
def solution(n):
    #문자열 sum사용
    #answer = sum(map(int, str(n)))
    #반복문 이용하기
    answer = 0
    li = list(str(int(n)))
    for i in range(len(li)):
        answer += int(li[i])
    return answer

#level1 3xN타일링
def solution(n):
    answer = [0,3,11]
    index = int(n/2)
    if n % 2 != 0: return 0
    if index < 3: return answer[index]
    for i in range(3, index+1):
        answer.append((3*answer[i-1]+sum(answer[1:i-1])*2+2)%1000000007)

    return answer[index]
