a,b,c=map(int,input("Enter the numbers: ").split())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)