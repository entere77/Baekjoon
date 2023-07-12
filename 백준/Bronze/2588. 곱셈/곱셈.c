#include<stdio.h>
int Num(void)
{
    int num;
    scanf("%d",&num);
    return num;
}

int main(void)
{
    int num1, num2;
    num1=Num();
    num2=Num();
    printf("%d\n", num1*(num2%10));//num1 x num2의 세번째 자릿수
    printf("%d\n", num1*((num2/10)%10));//num1 x num2의 두번째 자릿수
    printf("%d\n", num1*(num2/100));//num1 x num2의 첫번째 자릿수
    printf("%d\n", num1*num2);//num1 x num2의 결과값
    return 0;
}