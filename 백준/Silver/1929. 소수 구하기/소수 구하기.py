def check(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

primes=[]
m,n=map(int,input().split())

for i in range(m,n+1):
    if i==0 or i==1:
        continue
    if check(i):
        primes.append(i)

for prime in primes:
    print(prime)