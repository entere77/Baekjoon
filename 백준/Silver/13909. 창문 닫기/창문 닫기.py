n=int(input())
for i in range(1,46000):
    if i*i>n:
        print(i-1)
        break
    if i*i==n:
        print(i)
        break