import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
while True:
        try:    
            x1, y1, r1, x2, y2, r2 = input().split()
            x1=int(x1)
            x2=int(x2)
            r1=int(r1)
            r2=int(r2)
            y1=int(y1)
            y2=int(y2)
            d = ((x2-x1)**2+(y2-y1)**2)**0.5
            i=r1+r2
            if r1>r2:
                u=r1-r2
            else:
                u=r2-r1
            if i>=d>=u:
                print("YES")
            else:
                print("NO")
        except EOFError:
            break