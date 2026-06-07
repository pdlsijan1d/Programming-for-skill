#include<stdio.h>
int main()
{
    int n, count = 0, i;
    printf("enter a number:");
    scanf("%d",&n);
    
    for(i=1; i<=n; i++)
    {
        if(n%i==0)
        {
            count += 1;

        }
       
    }
    if(count==2)
    {
        printf("%d is prime", n);
    }
    else
    {
        printf("%d is composite",n);
    }
return 0;

}