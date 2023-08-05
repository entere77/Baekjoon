from itertools import combinations

n,m=map(int, input().split())
nums=[]
nums=list(map(int, input().split()))
res=combinations(nums,3)

gap=999999
least_sum=0
for j in (res):
    if sum(j)<=m:
        if m-(sum(j))<gap:
            gap=m-(sum(j))
            least_sum=sum(j)
print(least_sum)