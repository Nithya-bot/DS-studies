#armstrong number or not
def armstrong(n):
  TEMP=n
  sum=0
  while(n):
    num=n%10
    sum=sum+(num**3)
    n=n//10
  print('sum=',sum)
  if(sum==TEMP):
    return ('Armstrong number')
  else:
    return ('not Armstrong number')

a=armstrong(153)
print(a)
