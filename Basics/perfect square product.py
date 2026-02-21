#to multiply two numbers and find the product is a perfect square or not
N,M=map(int,input().split())
G=N*M
sqrt=G**0.5
if sqrt.is_integer():
    print('yes')
else:
    print('no')
