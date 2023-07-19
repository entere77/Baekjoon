n,m=map(int, input().split())
list=[0 for _ in range(n)]
for i in range(m):
    start,end,num=map(int, input().split())
    for j in range(start, end+1):
        list[j-1]=num
        
for k in range(n):
    print(list[k],end=' ')