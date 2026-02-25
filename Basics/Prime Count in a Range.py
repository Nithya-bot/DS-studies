# Problem Statement:
# Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).
###########################                     SIEVE METHOD              ####################################################

# Input Description:
# Input Size : L <= R <= 100000(complexity O(n) read about Sieve of Eratosthenes)


# Sample Input:
# 2 5


# Sample Output:
# 3

l,r=map(int,input().split())
prime=[True]*(r+1)

prime[0]=False
prime[1]=False

p=2
while p*p <= r:
  if prime[p]:
    for j in range(p*p,r+1,p):
      prime[j]=False
  p+=1
    
cnt=0
for i in range(l,r+1):
  if prime[i]:
    cnt+=1
print(cnt)
