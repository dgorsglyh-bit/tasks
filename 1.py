n=int(input())
if -10<n<10:
    n=n*n
    print(n)
else:
    n=n//10
    print(str(n*(n+1))+'25')