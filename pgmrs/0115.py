routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
#level3 단속카메라
def solution(routes):
    top = -30001
    cnt = 0
    routes.sort(key=lambda x: x[1])
    #그냥 routes.sort하면 안되고... 람다식으로 첫번째 원소를 기준으로 정렬해야함..
    print(routes)
    for i in routes:
        if i[0] > top:
            print(i[0],i[1])
            top = i[1]
            cnt += 1
    print(cnt)