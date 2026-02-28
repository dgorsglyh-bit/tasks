import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
while True:
    try:    
        a, b, c = input().split()
        a = int(a)
        b = int(b)
        c = int(c)
        if a<b<c or a<c<b:
            d = a//2
            print(d)
        if b<a<c or b<c<a:
            d =b//6
            print(d)
        if c<a<b or c<b<a:
            d=c//1
            print(d)
    except EOFError:
        break