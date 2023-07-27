n,b=map(int, input().split())
nums='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text=''
while(n): 
    text+=str(nums[n%b])
    n//=b
print(text[::-1])