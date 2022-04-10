#include <stdio.h>
#include<stdlib.h>
#define SIZE 5
struct QueueRecord
{
    int front;
    int rear;
    int array[SIZE];
};
typedef struct QueueRecord Queue;
int IsFULL(Queue);
int IsEmpty(Queue);
void Enqueue(Queue *,int);
int Dequeue(Queue *);
void display(Queue );
Queue CreateQueue();


Queue CreateQueue()
{
    Queue Q;
    Q.rear = - 1;
    Q.front = -1;
    return Q;
}


int IsFULL(Queue Q)
{
    if(((Q.rear + 1)%SIZE==Q.front) )
        return 1;
    else
        return 0;
}
int IsEmpty(Queue Q)
{
    if(Q.rear == -1)
        return 1;
    else
        return 0;
}

void Enqueue(Queue *Q,int element)
{
    if(IsFULL(*Q))
        printf("\n Queue is full!! \n");
    else
    {
        if(Q->front == -1)
            Q->front = 0;
        Q->rear = (Q->rear + 1) % SIZE;
        Q->array[Q->rear] = element;
        printf("\n Inserted -> %d", element);
    }
}


int Dequeue(Queue *Q)
{
    int element;
    if(IsEmpty(*Q)) 
    {
        printf("\n Queue is empty !! \n");
        return(-1);
    } 
    else 
    {
        element = Q->array[Q->front];

        if (Q->front ==Q-> rear)
	{
            Q->front = -1;
            Q->rear = -1;
        } /* Q has only one element, so we reset the queue after dequeing it. ? */
        else 
	{
            Q->front = (Q->front + 1) % SIZE;
        }

        printf("\n Deleted element -> %d \n", element);
        return(element);
    }
}




void display(Queue Q)
{
    int i;
    if(IsEmpty(Q))
        printf(" \n Empty Queue\n");
    else
    {
        //printf("\n Front -> %d ",Q.front);

        printf("\n Items -> ");

        for( i = Q.front; i!=Q.rear; i=(i+1)%SIZE) 
	{
            printf("%d ",Q.array[i]);
        }

        printf("%d ",Q.array[i]);
        //printf("\n Rear -> %d \n",Q.rear);
    }
}

int main()
{
    int i,ch,n,item,x;
    Queue Q;

   Q=CreateQueue();
   while(1)
   {
        printf("1-Insert\n2-Remove Element\n3-Display\n4-Exit\n");
        printf("Enter Choice\n");
        scanf("%d",&ch);

        switch(ch)
        {


            case 1: printf("Enter the element to be inserted\n");
                    scanf("%d",&item);
                    Enqueue(&Q,item);
                    break;

            case 2:x=Dequeue(&Q);
                    if(x!=-1)
                        {
                        printf("Removed Element is = %d\n",x);
                        }
                    break;

            case 3: display(Q);
                    break;

            case 4: exit(0);
                    break;
        }
    }

    return 0;
}
