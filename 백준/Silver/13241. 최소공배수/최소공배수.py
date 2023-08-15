def GCD(X,Y):
    while(Y):
        X,Y=Y,X%Y
    return X

a,b = map(int,input().split())
result = (a*b)//GCD(a,b)
print(result)