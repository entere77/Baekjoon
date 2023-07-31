x,y,w,h=map(int,input().split())
list_position=[]
min_value=9999999999999
length=0
for i in range(h+1):
    position=[w,i]
    list_position.append(position)
for j in range(w+1):
    position=[j,h]
    list_position.append(position)
for i in range(w+1):
    position=[i,0]
    list_position.append(position)
for j in range(h+1):
    position=[0,j]
    list_position.append(position)
for k in list_position:
    length=((x-k[0])**2+(y-k[1])**2)**(0.5)
    if min_value>length:
        min_value=length
print(int(min_value))