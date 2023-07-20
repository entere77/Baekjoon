n,m=map(int, input().split())
list=[i for i in range(1,n+1)]
for _ in range(m):
    i,j=map(int, input().split())
    minus=j-i+1
    for _ in range(minus//2):
        temp=list[i-1]
        list[i-1]=list[j-1]
        list[j-1]=temp
        j-=1
        i+=1
for i in range(n):
    print(list[i],end=' ')