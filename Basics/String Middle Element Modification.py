https://www.guvi.in/code-kata/string-middle-element-modification/
s=input()
l=len(s)
n=l//2
if l%2==1:
    print(s[0:n]+"*"+s[n+1:l])
else:   
    print(s[0:n-1]+'**'+s[n+1:l])
