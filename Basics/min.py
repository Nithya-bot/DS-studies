x=list(map(int, input().split()))
print(x)
min_far=5
for i in range(len(x)):
    if(x[i]<min_far):
        min_far=x[i]
print(min_far)