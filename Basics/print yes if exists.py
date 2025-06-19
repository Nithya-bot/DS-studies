N,K = map(int, input().split())
# Example: read n integers in one line
nums = list(map(int, input().split()))
if K in nums:
    print('yes')
else:
    print('no')