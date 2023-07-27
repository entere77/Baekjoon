n=int(input())
nums_list=[]
row=2
for i in range(0,15):
    row=row+(2**i)
    nums=row*row
    nums_list.append(nums)
print(nums_list[n-1])