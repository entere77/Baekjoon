n, a=map(int, input().split())
nums=list(map(int, input().split()))

for i in range(len(nums)):
    if nums[i]<a:
        print(nums[i],end=' ')