#include<stdio.h>

#define L 10

int DFS(int a[L][L],int v[L],int s,int n)
{
    int i;
    v[s]=1;
    printf("%d ",s+1);
    for(i=0;i<n;i++)
        if(a[s][i]==1 && v[i]==0)
            DFS(a,v,i,n);
    return 0;
}
int main()
{
    int j,i,n,v[L],a[L][L],s=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        v[i]=0;
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            scanf("%d",&a[i][j]);
    DFS(a,v,s,n);
}