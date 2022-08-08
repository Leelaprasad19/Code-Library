#include <stdio.h>
#include <string.h>

int stringSearch(char s[], int n, char key){
    
    for(int i=0;i < n;i++){
        if(s[i]==key){
            return i;
        }
    }
    
    return -1;
}

int main(void) {
	
	char s[100];
	
	scanf("%s", s);
	
	printf("%d",stringSearch(s, strlen(s), 'd'));
	
	return 0;
}

