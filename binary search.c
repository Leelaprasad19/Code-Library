#include <stdio.h>

int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;
 
        if (arr[mid] == x)
            return mid;
 
        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);
 

        return binarySearch(arr, mid + 1, r, x);
    }
 
    return -1;
}

void readArray(int arr[],int n){
    
    for(int i=0; i < n; i++){
        scanf("%d",&arr[i]);
    }
    
}
 
int main(void)
{
    int n,result,key;
    
    printf("Enter the number of elements : ");
    scanf("%d",&n);
    
    printf("Enter the key to be searched : ");
    scanf("%d",&key);
    
    int a[n];
    
    printf("Enter the elements in sorted order - \n");
    readArray(a,n);
    result = binarySearch(a, 0, n - 1, key);
    
    if(result != -1)
        printf("The element %d is present at index %d\n", key, result);
    else
        printf("The element %d is not present in the array\n");
        
    return 0;
}