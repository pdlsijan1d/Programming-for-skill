#include<stdio.h>
int main()
{
    int  n, num, digit, rev = 0 ;
    printf("Enter a number:");
    scanf("%d",&n);
    num = n;

    while(n != 0)
    {
        digit = n % 10;
        rev = rev*10 + digit;
        n = n/10;
    }

    if(rev==num)
        {
            printf("%d is palindrome.", num);
        }
    else
            printf("%d is not palindrome",num);
        
        
    
}    

