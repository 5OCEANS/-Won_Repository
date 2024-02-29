#11758- CCW

P1x,P1y = map(int,input().split())
P2x,P2y = map(int,input().split())
P3x,P3y = map(int,input().split())
a , b = 0, 0

res = P1x* P2y + P2x * P3y + P3x * P1y - P2x * P1y - P3x * P2y - P1x * P3y

if res>0:
    print(1)
elif res<0:
    print(-1)
else:
    print(0)

# if (P1x - P2x) == 0:
#     a = P1x
#     b = 0
# else:
#     g = (P2y-P1y)//(P2x-P1x)
#     a = g
#     b = -(g*P1x)+ P1y


# if (P3x * a + b) == P3y:
#     print(0)
# elif (P3x * a + b) > P3y:
#     print(-1)
# else:
#     print(1)

