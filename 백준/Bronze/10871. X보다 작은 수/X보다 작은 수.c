#include<stdio.h>
int Num(void)
{
    int num;
    scanf("%d",&num);
    return num;
}

int main(void)
{
    int num1,num2,su;
    num1=Num();
    num2=Num();
    
    for(int i=0;i<num1;i++)
    {
        scanf("%d", &su);
        if(su<num2)
        {
            printf("%d ", su);
        }
        else
            continue;
    }
    return 0;
    
}


