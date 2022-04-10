#include <stdio.h>
#include <limits.h>

struct node{
    struct node *left;
    struct node *right;
    int data;
};

typedef struct node *NODE;


void inOrder(NODE root){
    
    if(root==NULL){
        return;
    }else{
        
        inOrder(root->left);
        printf("%d ",root->data);
        inOrder(root->right);
        
    }
    
}

int count=0;

int function(NODE root)
{
    if (root == NULL) {
        return INT_MIN;
    }
 
    if (root->left == NULL && root->right == NULL)
    {
        count++;
        return root->data;
    }
 
    int left = function(root->left);
    int right = function(root->right);
 
    if ((left == INT_MIN && right == root->data) || (right == INT_MIN && left == root->data) || (left == right && left == root->data))
    {
        count++;
        return root->data;
    }
 
    return INT_MAX;
}

int countSubtrees(NODE root)
{
    function(root);
 
    return count;
}

NODE insert(NODE root,NODE data){
    
    if(root==NULL){
        root = data;
    }else{
        
        if(data->data < root->data){
            root->left = insert(root->left,data);
        }else{
            root->right = insert(root->right,data);
        }
        // else{
        //     printf("Duplicate Element - %d\n", data->data);
        // }
        
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
	    myData->left = NULL;
	    myData->right = NULL;
	    myData->data = data;
	    
	    root = insert(root,myData);
	    
	}

    inOrder(root);
    printf("%d ",countSubtrees(root));
	return 0;
}

