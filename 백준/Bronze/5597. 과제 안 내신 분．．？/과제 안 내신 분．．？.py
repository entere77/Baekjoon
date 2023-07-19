list=[i for i in range(1,31)]
for j in range(28):
    n=int(input())
    list[n-1]=0
for k in range(30):
    if list[k]!=0:
        print(list[k])