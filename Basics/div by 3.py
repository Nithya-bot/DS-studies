userInput = int(input())
n=userInput
sum=0
while(n):
    sum=sum+(n%10)
    n=n//10
if(sum%3==0): print("yes")
else: print("not")
