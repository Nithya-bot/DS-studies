N=int(input())
rev=0
while(N):
    num=N%10
    rev=(rev*10)+num
    N=N//10
print(rev)
