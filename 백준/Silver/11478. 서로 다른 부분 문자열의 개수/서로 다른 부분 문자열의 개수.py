n = list(input())
a= []
for i in range(1,len(n)):
    for j in range(0,len(n)):
        a.append(''.join(n[j:j+i]))
a=set(a)
print(len(a)+1)