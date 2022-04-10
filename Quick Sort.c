//
//  main.c
//  QuickSort
//
//  Created by MAP on 3/2/21.
//

#include <stdio.h>

#define L 10

int a[L];

int QuickSort(int l,int h)
{
    int i,j,pi,t;
    
    if(l < h)
    {
        pi=l;
        i=l;
        j=h;
        
        while(i < j)
        {
            while(a[i] <= a[pi] && i < h)
                i++;
            
            while (a[j] > a[pi])
                j--;
            
            if(i < j)
            {
                t = a[i];
                a[i] = a[j];
                a[j] = t;
            }
        }
        
        t = a[j];
        a[j] = a[pi];
        a[pi] = t;
        
        QuickSort(l, j-1);
        QuickSort(j+1, h);
    }
    return 0;
}

int main()
{
    int i,n;
    
    printf("Enter the number of elements : ");
    scanf("%d",&n);
    
    for (i=0;i<n;i++)
        scanf("%d",&a[i]);
    
    QuickSort(0,n-1);
    
    for (i=0; i<n; i++)
        printf("%d ",a[i]);
    printf("\n");
    
    return 0;
}
