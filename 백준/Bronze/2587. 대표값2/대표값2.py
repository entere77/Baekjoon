nums=[]
for i in range(5):
    nums.append(int(input()))
nums=sorted(nums)
mean=sum(nums)//5
middle=nums[2]
print(mean)
print(middle)