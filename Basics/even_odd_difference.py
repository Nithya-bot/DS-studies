# Problem Statement:
# Given 2 numbers N,M. Find their difference and check whether it is even or odd.


# Sample Input:
# 5 5


# Sample Output:
# even

N,M=map(int,input().split())
if(abs(M-N)%2!=0):
    print('odd')
else:
    print('even')
