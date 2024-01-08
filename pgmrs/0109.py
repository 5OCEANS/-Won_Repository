#level1 2018 KAKAO BLIND RECRUITMENT [1차] 비밀지도
def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        strings = ""
        li1 = list(bin(arr1[i])[2:])
        while(len(li1)<n):
            li1.insert(0,'0')
        li2 = list(bin(arr2[i])[2:])
        while(len(li2)<n):
            li2.insert(0,'0')
        print(li1)
        print(li2)

        for j in range(n):
            if li1[j] == '0' and li2[j]=='0':
                strings += ' '
            else:
                strings += '#'
        answer.append(strings)
    print(answer)
                         
    return answer

#level1 월간코드챌린지 시즌1 내적
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += (a[i] * b[i])
        
    return answer


