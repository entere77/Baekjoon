A,B,V=map(int, input().split())
day_height=(A-B)
real_height=(V-A)
day=1
if (real_height)%(day_height)==0:
    day+=(real_height)//(day_height)
else:
    day+=(real_height)//(day_height)+1
print(day)