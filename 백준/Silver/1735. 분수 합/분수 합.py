def GCD(X,Y):
    while(Y):
        X,Y=Y,X%Y
    return X
    
a1,b1=map(int, input().split())
a2,b2=map(int, input().split())

share=(b1*b2)//GCD(b1,b2)
mul_num1=(share//b1)*a1     #첫번째 입력 분자
mul_num2=(share//b2)*a2     #두번째 입력 분자

min_num=GCD((mul_num1+mul_num2), share)

numerator=(mul_num1+mul_num2)//min_num
denominator=(share)//min_num

print(numerator, denominator)