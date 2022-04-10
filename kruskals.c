#include <stdio.h>
#define L 20

struct node
{
    int u,v,w;
};
typedef struct node NODE;

int read(NODE a[L],int n);
int display(NODE a[L],int n);
int compute(NODE a[L],int n,int u[L],int e);
int unionArray(int u[L],int n);
int DisplayUnionArray(int u[L],int n);
int find(NODE a[L],int i,int u[L]);
int sort(NODE a[L],int n);

int main(void) 
{
    int n=14,u[L],e=9,weight;
    NODE a[L];
    read(a,n);
    sort(a,n);
    unionArray(u,e);
    //DisplayUnionArray(u,e);
    weight=compute(a,n,u,e);
    //display(a,n);
    printf("\nWeight = %d",weight);
}
int read(NODE a[L],int n)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        scanf("%d %d %d",&a[i].u,&a[i].v,&a[i].w);
    }
    return 0;
}
int compute(NODE a[L],int n,int u[L],int e)
{
    int i,weight=0;
    printf("The Selected nodes are : ");
    for(i=0;i<n;i++)
    {
        if(find(a,i,u))
        {
            weight+=a[i].w;
            printf("(%d,%d)=%d, ",a[i].u,a[i].v,a[i].w);
            DoUnion(u,e,a[i].u,a[i].v);
        }
        //printf("iter %d : ",i+1);
        //DisplayUnionArray(u,e);
    }
    return weight;
}
int DoUnion(int u[L],int e,int e1,int e2)
{
    int i,t;
    t=u[e1];
    for(i=0;i<e;i++)
    {
        if(u[i]==t)
            u[i]=u[e2];
    }
    return 0;
}
int find(NODE a[L],int i,int u[L])
{
    if(u[a[i].u]==u[a[i].v])
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
int unionArray(int u[L],int n)
{
    for(int i=0;i<n;i++)
    {
        u[i]=i;
    }
    return 0;
}
int DisplayUnionArray(int u[L],int n)
{
    for(int i=0;i<n;i++)
    {
        printf("%d ",u[i]);
    }
    printf("\n");
    return 0;
}
int sort(NODE a[L],int n)
{
    int i,j;
    NODE temp;
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-1-i;j++)
        {
            if(a[j].w>a[j+1].w)
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
    }
    return 0;
}
int display(NODE a[L],int n)
{
    int i;
    for(i=0;i<n;i++)
    {
        printf("%d %d %d\n",a[i].u,a[i].v,a[i].w);
    }
    return 0;
}