# Problem Statement:
# Given 3 numbers A,B,C find the sum of Arithmetic Series with a=A, d=B and n=C


# Sample Input:
# 1 1 2


# Sample Output:
# 3

a,d,n=map(int,input().split())
k=n * (2*a + (n-1)*d) / 2
print(int(k))
