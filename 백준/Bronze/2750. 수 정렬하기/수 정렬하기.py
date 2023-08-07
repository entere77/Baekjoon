n=int(input())
nums=[]
for i in range(n):
    nums.append(int(input()))

nums=sorted(nums)
for i in range(n):
    print(nums[i])