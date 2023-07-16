price=int(input())
n=int(input())
sum=0
for i in range(1,n+1):
    a, b=map(int, input().split())
    sum+=a*b
    
if sum==price:
    print('Yes')
else:
    print('No')