n=int(input())
area=0
total=[[0 for _ in range(100)] for _ in range(100)]
for i in range(n):
    x,y=map(int, input().split())
    for j in range(x,x+10):
        for k in range(y,y+10):
            total[j][k]=1
for i in range(100):
    area+=total[i].count(1)
print(area)