n=int(input())
nums=1
while(n>nums):
    n-=nums
    nums+=1

if nums%2==0:
    a=n
    b=nums-n+1
else:
    a=nums-n+1
    b=n
print(a,'/',b,sep='')