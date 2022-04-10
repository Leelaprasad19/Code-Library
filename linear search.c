#include <stdio.h>

int linearSearch(int arr[], int n, int key)
{
    for(int i=0;i<n;i++){
        
        if(arr[i]==key){
            return i;
        }
        
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
    result = linearSearch(a, n, key);
    
    if(result != -1)
        printf("The element %d is present at index %d\n", key, result);
    else
        printf("The element %d is not present in the array\n");
        
    return 0;
}