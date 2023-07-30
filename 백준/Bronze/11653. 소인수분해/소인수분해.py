n=int(input())
prime_list=[]
if n==1:
    pass
else:
    i=2
    while(n!=1):
        if n%i==0:
            prime_list.append(i)
            n=n//i
        else:
            i+=1
for num in prime_list:
    print(num)