#include <stdio.h>
#include<limits.h>

#define L 10
#define A 20

struct node
{
    int dist,path;
};

typedef struct node NODE;
 
int read(int cost[L][L],int n);
int display(int cost[L][L],int n);
int displayLoaded(NODE a[A],int n,int visited[A]);
int Load(int cost[L][L],NODE a[A],int n,int sv,int visited[A]);
int minimum(NODE a[A],int n,int visited[A]);
int compute(int cost[L][L],NODE a[A],int visited[A],int n);
int iteration(int cost[L][L],NODE a[A],int n,int visited[A],int ind);
int MST(NODE a[A],int n);

int main() 
{
    int cost[L][L],n=9,sv=0,visited[A],weight;
    NODE a[A];
    
    read(cost,n);
    Load(cost,a,n,sv,visited);
    compute(cost,a,visited,n);
    //displayLoaded(a,n,visited);
    weight=MST(a,n);
    printf("Weight=%d",weight);
    //display(cost,n);
	return 0;
}
int read(int cost[L][L],int n)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&cost[i][j]);
        }
    }
    return 0;
}
int Load(int cost[L][L],NODE a[A],int n,int sv,int visited[A])
{
    int i;
    for(i=0;i<n;i++)
    {
        a[i].dist=cost[sv][i];
        a[i].path=sv;
        visited[i]=0;
    }
    visited[sv]=1;
    return 0;
}
int compute(int cost[L][L],NODE a[A],int visited[A],int n)
{
    int i,ind;
    for(i=0;i<n-1;i++)
    {
        ind=minimum(a,n,visited);
        iteration(cost,a,n,visited,ind);
        //printf("\nIter %d\n",i+1);
        //displayLoaded(a,n,visited);
        //printf("%d ",ind+1);
    }
    return 0;
}
int iteration(int cost[L][L],NODE a[A],int n,int visited[A],int ind)
{
    int i;
    for(i=0;i<n;i++)
    {
        if(!visited[i] && cost[ind][i]<a[i].dist)
        {
            a[i].dist=cost[ind][i];
            a[i].path=ind;
        }
    }
    return 0;
}
int minimum(NODE a[A],int n,int visited[A])
{
    int i,min=INT_MAX,ind;
    for(i=0;i<n;i++)
    {
        if(!visited[i] && min > a[i].dist)
        {
            min=a[i].dist;
            ind=i;
        }
    }
    visited[ind]=1;
    return ind;
}
int MST(NODE a[A],int n)
{
    int i,weight=0;
    for(i=0;i<n;i++)
    {
        weight+=a[i].dist;
    }
    return weight;
}
int displayLoaded(NODE a[A],int n,int visited[A])
{
    int i;
    for(i=0;i<n;i++)
    {
        printf("%d %d %d\n",a[i].dist,a[i].path,visited[i]);
    }
    return 0;
}
int display(int cost[L][L],int n)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%3d ",cost[i][j]);
        }
        printf("\n");
    }
    return 0;
}