# Problem Statement:
# Find the minimum among 10 numbers.


# Input Description:
# The input consists of 10 space-separated integers.


# Output Description:
# The output is the minimum of the given 10 integers.


# Sample Input:
# 5 4 3 2 1 7 6 10 8 9


# Sample Output:
# 1
#without library
arr = list(map(int, input().split()))
min=arr[0]
for x in arr:
    if x < min:
        min=x
print(min)

#with library
arr = list(map(int, input().split()))
arr.sort()
print(arr[0])
