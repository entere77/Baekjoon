m=int(input())
n=int(input())
prime_list=[]
my_sum=0
for num in range(m,n+1):
    mod_list=[]
    for i in range(2,num):
        if num%i==0:
            mod_list.append(i)
    if len(mod_list)==0:
        if num!=1:
            prime_list.append(num)
            my_sum+=num
if len(prime_list)==0:
    print(-1)
else:
    print(my_sum)
    print(min(prime_list))