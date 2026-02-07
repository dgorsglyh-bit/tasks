m1, m2, m3 = input().split()
m1 = int()
m2 = int()
m3 = int()
if 94<=m1<=727 and 94<=m2<=727 and 94<=m3<=727:
    if m1>m2:
        if m1>m3:
            print(m1)
        else:
            print(m3)
    else:
        if m2>m3:
            print(m2)
        else:
            print(m3)
else:
    print("Error")


