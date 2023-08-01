n=int(input())
pos_x=[]
pos_y=[]
for i in range(n):
    x,y=map(int, input().split())
    pos_x.append(x)
    pos_y.append(y)

max_x=max(pos_x)
max_y=max(pos_y)
min_x=min(pos_x)
min_y=min(pos_y)
print((max_x-min_x)*(max_y-min_y))