n1, n2=map(int, input().split())
num1=1
num2=1
for i in range(n2):
    num1*=n1
    n1-=1
for j in range(n2,0,-1):
    num2*=j
    
print(num1//num2)