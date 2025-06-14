# check a number is palindrome with lesser time complexity

def is_pal(n):
    if(n<0): return False
    num=n
    rev=0
    while(num):
        r=num%10
        rev=(rev*10)+r
        num=num//10
    print("rev", rev)
    if(rev==n): return True
    else: return False
number=int(input())
s=is_pal(number)
print(s)