#4153 직각삼각형
while True:
    num = list(map(int, input().split()))

    if sum(num) == 0:
        break
    res = max(num)
    num.remove(res)

    if num[0]**2 + num[1]**2 == res**2:
        print('right')
    else:
        print('wrong')
