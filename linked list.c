#include <stdio.h>

struct node{
    struct node *right;
    int data;
};

typedef struct node *NODE;

NODE insert(NODE root,NODE data){
    
    if(root==NULL){
        root = data;
    }else{
        
        NODE c = root;
        
        while(c->right!=NULL){
            c = c->right;
        }
        
        c->right = data;
    }
    
    return root;
    
}

int main(void) {
	
	int n,data;
	NODE root=NULL,myData;
	
	scanf("%d", &n);
	
	
	for(int i=0;i<n;i++){
	    
	    scanf("%d", &data);
	    
	    myData = (NODE*)malloc(sizeof(struct node));
	    myData->right = NULL;
	    myData->data = data;
	    
	    root = insert(root,myData);
	    
	}
    
    NODE c = root;
    while(c!=NULL){
        
        printf("%d ",c->data);
        c = c->right;
        
    }
	return 0;
}

