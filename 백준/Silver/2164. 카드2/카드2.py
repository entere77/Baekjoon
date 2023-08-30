from collections import deque
n=int(input())
nums=deque([i for i in range(1,n+1)])
temp=0
while len(nums)>1:
    nums.popleft()
    nums.append(nums.popleft())
print(nums[-1])       