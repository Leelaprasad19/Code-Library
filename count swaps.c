#include <math.h>
#include <stdio.h>
 
void insertionSort(int arr[], int n)
{
    int i, key, j,count = 0;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
 
        while (j >= 0 && arr[j] > key) {
            count = count + 1;
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
    
    printf("%d\n",count);
    if(count >= n)
        printf("YES\n");
    else
        printf("NO\n");
}
 
void printArray(int arr[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        scanf("%d", &arr[i]);
}
 
int main()
{
    int n,q;
 
    scanf("%d",&q);
    
    while(q--){
     
        scanf("%d",&n);
        int arr[n];

        printArray(arr, n);
        insertionSort(arr, n);
        
    }
 
    return 0;
}