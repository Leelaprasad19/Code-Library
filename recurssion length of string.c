#include <stdio.h>

int stringLength(char s[]){
    
    int i = 0;
    
    while(s[i]!='\0'){
        i+=1;
    }
    
    return i;
}

int main() {
	
	char s[100];
	
	scanf("%s", s);
	
	printf("%d",stringLength(s));
	
	return 0;
}

