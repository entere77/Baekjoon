n=int(input())
nums=list(map(int,input().split()))
count=0
for num in nums:
    mod_list=[]
    for i in range(1,num+1):
        if num%i==0:
            mod_list.append(i)
    if len(mod_list)==2:
        count+=1
print(count)