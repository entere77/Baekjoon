t = int(input())

def GCD(X,Y):
    while(Y):
        X,Y=Y,X%Y
    return X

for i in range(t):
    a,b = map(int,input().split())

    result = (a*b)//GCD(a,b)
    print(result)