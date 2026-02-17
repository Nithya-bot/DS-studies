#armstrong number or not
n=int(input())
TEMP=n
sum=0
while(n):
  num=n%10
  sum=sum+(num**3)
  n=n//10
print('sum=',sum)
if(sum==TEMP):
  print('Armstrong number')
else:
  print('not Armstrong number')
