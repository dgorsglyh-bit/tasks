n = int(input())
if n>0:
    while n%2==0:
        n=n/2
    if n>1:
        print("NO")
    else:
        print("YES")
else:
    print("NO")
