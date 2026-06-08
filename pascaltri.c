#include<stdio.h>
int main()
{
    int i, j, n;
    
    printf("Enter the number of rows you want:");
    scanf("%d", &n);
    int triangle[n][n];

    for(i = 0; i<n; i++)
    {
        for(j=0; j<=i; j++)
        {
            if(i == 0 || j == i)
            {
                triangle[i][j] = 1;  
            }
            else
            {
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j];
            }

        }
    }

    for(i=0;i<n;i++)
    {
        for(j=0; j<=i; j++)
        {
            printf("%d", triangle[i][j]);

        }
        printf("\n");
    }

    return 0;


}