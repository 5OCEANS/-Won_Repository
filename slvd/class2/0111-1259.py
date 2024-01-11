
while True :
    st = list(input())
    if st == ['0']:
        break
    str = st.copy()
    str.reverse()
    print(st,str)
    if st == str:
        print("yes")
    else:
        print("no")