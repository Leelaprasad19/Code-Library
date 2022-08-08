#include <stdio.h>
#include <string.h>

int primeInRange(int n){
    
    int a[n+1];
    
    for(int i=0; i<=n; i++)
        a[i] = 1;
    
    int p = 2;
    
    while(p * p <= n){
        
        if(a[p]){
            for(int i = p * p ; i <= n; i += p)
                a[i] = 0;
        }
        
        p += 1;
        
    }
    
    
    for(int i = 2; i <= n; i++){
        if(a[i]){
            printf("%d ", i);
        }
    }
    
}

int main() {
	
	primeInRange(200);
	
	return 0;
}

