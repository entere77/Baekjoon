n=int(input())
start=1
num_rooms=1
while(n>start):
    start+=6*num_rooms
    num_rooms+=1
print(num_rooms)