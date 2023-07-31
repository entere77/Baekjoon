pos_x=[]
pos_y=[]
x_value=0
y_value=0
for i in range(3):
    x,y=map(int, input().split())
    pos_x.append(x)
    pos_y.append(y)
for i in range(3):
    if pos_x.count(pos_x[i])==1:
        x_value=pos_x[i]
    if pos_y.count(pos_y[i])==1:
        y_value=pos_y[i]
print(x_value, y_value)