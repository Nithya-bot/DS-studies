# Problem Statement:
# Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.


# Sample Input:
# 6 2
# 1 2 3 5 7 8


# Sample Output:
# 1


N,K=map(int,input().split())
arr = list(map(int, input().split()))
cnt=0
for i in range (0,N):
    if(arr[i]==K):  
        cnt+=1
if cnt>0:
    print(cnt)
else:
    print('-1')
