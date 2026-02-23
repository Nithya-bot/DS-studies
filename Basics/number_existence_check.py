# Problem Statement:
# Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.


# Input Description:
# The input consists of two integers, N and K, followed by N integers.


# Output Description:
# The output is 'yes' if K is found among the N integers, otherwise 'no'.


# Sample Input:
# 4 2
# 1 2 3 3


# Sample Output:
# yes

N,K=map(int,input().split())
arr = list(map(int, input().split()))

for i in range (0,N):
    if(arr[i]==K):  
        print('yes')
        break
else:
    print('no')
