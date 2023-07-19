n,m=map(int, input().split())
list=[i for i in range(1,n+1)]
temp=0
for j in range(m):
    c1,c2=map(int, input().split())
    temp=list[c1-1]
    list[c1-1]=list[c2-1]
    list[c2-1]=temp
    
for k in range(n):
    print(list[k], end=' ')