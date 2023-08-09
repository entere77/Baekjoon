n=int(input())
pos=[]
for i in range(n):
    pos.append(list(map(int, input().split())))

temp=0
for j in range(n):
    temp=pos[j][0]
    pos[j][0]=pos[j][1]
    pos[j][1]=temp

pos.sort()
for j in range(n):
    temp=pos[j][0]
    pos[j][0]=pos[j][1]
    pos[j][1]=temp

for k in pos:
    print(k[0],k[1])