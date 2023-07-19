max=0
index=0
for i in range(1, 10):
    num=int(input())
    if max<num:
        max=num
        index=i
print(max)
print(index)