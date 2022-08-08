#include <stdio.h>
#include <string.h>

int reverse(int num){
    
    int sol = 0;
    
    while(num){
        
        sol = sol * 10 + num % 10;
        num = num / 10;
        
    }
        
    return sol;
    
}

int main() {
	
	int num = 343;
	
	int rev = reverse(num);
	
	if(num==rev)
	    printf("The number is palindrome\n");
	else
	    printf("The number is not palindrome\n");
	    
	
	return 0;
}

