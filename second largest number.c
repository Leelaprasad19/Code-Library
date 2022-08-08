#include <stdio.h>
#include <string.h>
#include <limits.h>

int secondLargestNumber(int a[], int n){
    
    int max1 = INT_MIN, max2 = INT_MIN;
    
    for(int i=0; i<n; i++){
        
        if(a[i] > max1){
            max2 = max1;
            max1 = a[i];
        }else if(a[i] > max2){
            max2 = a[i];
        }
        
    }
    
    printf("%d %d", max1, max2);
        
    return 0;
    
}

int main() {
	
	int n, a[100];
	
	scanf("%d", &n);
	
	for(int i=0; i<n; i++)
	    scanf("%d", &a[i]);
	    
	printf("%d\n", a[n-1]);
	    
	secondLargestNumber(a, n);
	
	return 0;
}

