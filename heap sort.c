#include <stdio.h>

#define L 10

int h[L],n;

int heapify(int i)
{
    int largest = i;
    int left = 2*i+1;
    int right = 2*i+2;
    
    if(left < n && h[left] > h[largest])
        largest = left;
    if(right < n && h[right] > h[largest])
        largest = right;
    
    if(largest!=i)
    {
        int temp = h[i];
        h[i] = h[largest];
        h[largest] =temp;
        heapify(largest);
    }
    return 0;
}
int heapSort()
{
    int i,temp,t=n;
    
    for (i=n/2-1; i>=0; i--)
        heapify(i);
    
    for (i=n-1; i>=0; i--) {
        temp=h[i];
        h[i]=h[0];
        h[0]=temp;
        n--;
        heapify(0);
    }
    
    return  t;
}

int main()
{
    
    int i,t;
    printf("Enter the number of elements : ");
    scanf("%d",&n);
    t=n;
    for (i=0; i<n; i++)
        scanf("%d",&h[i]);
    
    n=heapSort();
        
    for (i=0; i<n; i++)
        printf("%d ",h[i]);
        
    printf("\n");
    
    return 0;
}