#include <stdio.h>
#include<stdlib.h>

#define L 10

struct queue
{
    int data;
    struct queue *next;
};
typedef struct queue *Q;

Q CreateQueue(int data);
Q insert(Q first,int data);
int display(Q first);

int ReadMatrix(int a[L][L],int n);
int Matrix(int a[L][L],int n);

Q BFS(int a[L][L],Q first,int n);
int AllVisited(int v[L],int n);
int InQueue(Q first,int s);
Q dequeue(Q first,int *s);
int DisplayVisited(int v[L],int n)
{
    int i;
    printf("\n");
    for(i=0;i<n;i++)
    printf("%d ",v[i]);
    printf("\n");
}

int main(void) 
{
    int a[L][L],n;
    Q first=NULL;
    
    scanf("%d",&n);
    ReadMatrix(a,n);
    first=BFS(a,first,n);
	return 0;
}
Q BFS(int a[L][L],Q first,int n)
{
    int i,v[L],s=0;
    for(i=0;i<n;i++)
        v[i]=0;
    v[s]=1;
    first=insert(first,s);
    
    for(int j=0;j<n;j++)
    {
        for(i=0;i<n;i++)
        {
            if(a[s][i]==1 && !InQueue(first,i) && v[i]==0)
                first=insert(first,i);
        }
        first=dequeue(first,&s);
        printf("%d ",s+1);
        v[s]=1;
    }
    return first;
}
Q dequeue(Q first,int *s)
{
    int temp;
    if(first==NULL)
        return NULL;
    temp=first->data;
    *s=temp;
    first=first->next;
    return first;
}
int InQueue(Q first,int s)
{
    while(first!=NULL)
    {
        if(first->data==s)
            return 1;
        first=first->next;
    }
    return 0;
}
int ReadMatrix(int a[L][L],int n)
{
    int i,j;
    
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
}
Q insert(Q first,int data)
{
    Q temp,c;
    temp=CreateQueue(data);
    if(first==NULL)
    {
        return temp;
    }
    else
    {
        c=first;
        while(c->next!=NULL)
        {
            c=c->next;
        }
        c->next=temp;
    }
    return first;
}
Q CreateQueue(int data)
{
    Q temp;
    temp=(struct queue*)malloc(sizeof(struct queue));
    temp->next=NULL;
    temp->data=data;
    return temp;
}
int display(Q first)
{
    printf("\n");
    while(first!=NULL)
    {
        printf("%d ",first->data);
        first=first->next;
    }
    printf("\n");
    return 0;
}
