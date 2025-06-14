userInput=int(input())
n=userInput
sum=0
maxsum=0
while(n):
    r=n%10
    n=n//10
    if r==1: sum+=1
    if r==0:
        if(sum>maxsum):
            maxsum=sum
            sum=0

if maxsum==0: print(-1)
else:
    print(maxsum)