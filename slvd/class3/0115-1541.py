#1541 잃어버린 괄호

#-를 기준으로 묶어서 list만들기
nlist = list(input().split('-'))
#정답 저장용
answer = 0
#list의 원소마다!
for i in nlist:
    #안에서 +를 기준으로 자르기
    nli = i.split('+')
    #자른 str배열 int배열로 만들기
    num = list(map(int,nli))
    #==대신 is를 사용해 list의 첫번째 값인지 확인한다고 생각했는데... 틀렸다네
    if i is nlist[0]:
        #첫번째 값은 답에서 더하기
        answer += sum(num)
    else:
        #두번째 값부터는 
        answer -= sum(num)
print(answer)

#리스트 첫번째 값을 따로 계산하고 for문에 1:로 슬라이싱 리스트로 넣기
nlist = list(input().split('-'))

nli = nlist[0].split('+')
num = list(map(int,nli))
answer = sum(num)

for i in nlist[1:]:
    #안에서 +를 기준으로 자르기
    nli = i.split('+')
    #자른 str배열 int배열로 만들기
    num = list(map(int,nli))
    #==대신 equal을 사용해 list의 첫번째 값인지 확인
    #두번째 값부터는 
    answer -= sum(num)
print(answer)



    
    
