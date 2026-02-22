#in a number 1234, print 1 3
#if no odd digits present, print -1

#change int as string and strip the digits. 
#when work on individual digits, treat as int as in line 12 and append in empty list
#while print list, join using the space
N = input().strip()

odd_digits = []

for d in N:
    if int(d) % 2 != 0:
        odd_digits.append(d)

if odd_digits:
    print(" ".join(odd_digits))
else:
    print(-1)
