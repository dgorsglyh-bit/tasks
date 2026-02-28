import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
while True:
    try:    
        a, b ,c =input().split()
        a =int(a)
        b =int(b)
        c =int(c)
        if a>c*2 and b>c*2:
            print("YES")
        else:
            print("NO")

    except EOFError:
            break