# Problem Statement:
# Given a number N, print the product of the digits.


# Input Description:
# Input Size : N <= 100000000000


# Sample Input:
# 2143


# Sample Output:
# 24



N=input().strip()
d=[]
mul=1
for d in N:
    mul=mul*int(d)
print(mul)
