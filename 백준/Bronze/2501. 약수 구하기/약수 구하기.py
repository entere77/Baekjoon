n,k=map(int,input().split())
factor_list=[]
for i in range(1,n+1):
    if n%i==0:
        factor_list.append(i)

if k>len(factor_list):
    print(0)
else:
    print(factor_list[k-1])