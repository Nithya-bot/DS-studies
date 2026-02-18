s=input()
#prints whether vowel is present or not
for word in s:
    if(word=='a' or word=='e' or word=='i' or word=='o' or word=='u'):
        print('yes')
        break
else:
    print('no')
