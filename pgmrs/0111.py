#level1 자연수 뒤집어 배열만들기
def solution(n):
    answer = list(str(n))
    answer.reverse()
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    return answer

#level1 문자열 내 p와 y의 개수
def solution(s):
    s = s.lower()
    p = s.count("p")
    y = s.count("y")
    if p == y:
        return True
    return False

#level1 제일 작은 수 제거하기
def solution(arr):
    if len(arr) <= 1:
        arr.clear()
        arr.append(-1)
    else:
        arr.remove(min(arr))
    return arr
