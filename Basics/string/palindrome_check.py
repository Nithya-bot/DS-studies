https://www.guvi.in/code-kata/palindrome-check/
s=input()

for i in range(len(s)//2):
    if(s[i]!=s[len(s)-i-1]):
        print('no')
        break
else:
    print('yes')
