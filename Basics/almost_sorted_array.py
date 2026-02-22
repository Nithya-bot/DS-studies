#Problem Statement:
# Given a number N followed by N elements which can be arranged in ascending order with maximum one element update. Print the index of the element which has to be changed else print '-1' if the updation not neccassary or if the given input needs more than one update to form ascending order.


# Sample Input:
# 7
# 1 2 4 3 5 6 8
# 5
# 1 10 3 14 5


# Sample Output:
# 2

n = int(input())
arr = list(map(int, input().split()))
cnt=0
m=0
for i in range (0,n-1):
    if(arr[i]>arr[i+1]):
      cnt+=1
      m=i
if(cnt>1 or cnt==0):
  print(-1)
elif(cnt==1):
  print(m)
