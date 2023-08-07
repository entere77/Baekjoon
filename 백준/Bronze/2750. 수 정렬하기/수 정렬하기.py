n=int(input())
nums=[]
for i in range(n):
    nums.append(int(input()))

for j in range(n):
    min_index=j
    for k in range(j+1,n):
        if nums[min_index]>nums[k]:
            min_index=k
    nums[j], nums[min_index] = nums[min_index], nums[j]
for k in range(n):
    print(nums[k])