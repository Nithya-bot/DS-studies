# Problem Statement:
# Write a program to print the sum of the first K natural numbers.


# Input Description:
# Input Size : n <= 100000


# Sample Input:
# 3


# Sample Output:
# 6

N=int(input())
sum=0
for i in range(1,N+1):
    sum=sum+i
print(sum)
