#include<stdio.h>
int main()
{
    int n;
    printf("Enter the number of terms you want:");
    scanf("%d",&n);
    int i, a=0, b=1, c;
    printf("The required fibonacci series is:\n");
    printf("%d\t",a);
    printf("%d\t",b);
    for(i=0; i<=n; i++)
    {
        
        a=b;
        b=c;
        c=a+b;
        printf("%d\t",c);
    }
    
    return 0;
}




