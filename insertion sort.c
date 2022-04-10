//
//  main.c
//  InsertionSort
//
//  Created by MAP on 2/28/21.
//

#include <stdio.h>

#define L 10

int a[L],i,n;

int InsertionSort()
{
    int temp,j;
    for (i=1; i<n; i++)
    {
        temp=a[i];
        j=i-1;
        while (j>=0 && a[j] > temp)
        {
            a[j+1]=a[j];
            j--;
        }
        a[j+1]=temp;
    }
    return 0;
}

int main()
{
    scanf("%d",&n);
    for (i=0;i<n;i++) {
        scanf("%d",&a[i]);
    }
    InsertionSort();
    for (i=0; i<n; i++) {
        printf("%d ",a[i]);
    }
    printf("\n");
    return 0;
}
