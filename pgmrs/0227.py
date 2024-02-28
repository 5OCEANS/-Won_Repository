def solution(babbling):
    score = 0
    bab = ["ayaaya","yeye","woowoo","mama"]
    #발음한 내용 하나하나에 적용
    for i, search in enumerate(babbling):
        if search in bab:
            continue
        else:
            #길이가 다른경우
            #word에서 삭제하고 돌아가기
            search = search.replace("aya",'1',1).replace("ye",'1',1).replace("woo",'1',1).replace("ma",'1',1)
            babbling[i] = search
            print(babbling[i])
            if search.isdigit():
                #점수추가
                score+=1
    return score
                    
babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]           
                    
sc = solution(babbling)
print(sc)