# to sum two values in two pointer method


input_array_of_strings=input("enter integer array: ")
List_of_numbers=numbers = list(map(int, input_array_of_strings.split()))
target=int(input())

def twoSum(nums, t):
        A=[]
        n=len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if(nums[i]+nums[j]==t):
                    A.append(i)
                    A.append(j)
        return A

s=print(twoSum(List_of_numbers, target))
    

