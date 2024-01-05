#크레인 인형뽑기 게임
def solution(board, moves):
    #stack만들기
    stack = []
    #답저장용
    answer = 0
    #리스트 안에 있는 모든 원소 한번씩
    for i in moves:
        for j in range(len(board)):
            #실제 배열은 0부터 시작하니까 i-1
            if board[j][i-1] != 0:
                #0이 아닌 무언가가 있으면 stack에 집어넣기
                stack.append(board[j][i-1])
                #비어있는 칸으로 변경
                board[j][i-1] = 0
                #두개 이상 들어가 있을때
                if len(stack) > 1:
                    #가장 최근 입력한 두 원소가 같은 값인 경우
                    if stack[-1] == stack[-2]:
                        #stack에서 제거하기
                        stack.pop(-1)
                        stack.pop(-1)
                        #정답에 2점추가
                        answer += 2
                #다음 moves로 넘어가기 위해 더 내려가지말고 break걸기!!
                break
                
    return answer
