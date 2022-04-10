#include <stdio.h>
#define L 5

int read(int a[L][L],int n);
int display(int a[L][L],int n);
int compute(int a[L][L],int n);

int main(void) 
{
    int a[L][L],n=4;
    read(a,n);
    compute(a,n);
    display(a,n);
}
int read(int a[L][L],int n)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    return 0;
}
int compute(int a[L][L],int n)
{
    int f,i,j,t;
    for(f=0;f<n;f++)
    {
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(i!=f && j!=f)
                {
                    if(a[i][j]!=1)
                    a[i][j]=a[i][f] & a[f][j];
                }
            }
        }
    }
    return 0;
}
int display(int a[L][L],int n)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
    return 0;
}