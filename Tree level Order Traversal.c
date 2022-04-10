#include <stdio.h>

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

NODE insert(NODE root,NODE data){
    
    if(root==NULL){
        root = data;
    }else{
        
        if(data->data < root->data){
            root->left = insert(root->left,data);
        }else if(data->data > root->data){
            root->right = insert(root->right,data);
        }else{
            printf("Duplicate Element - %d\n", data->data);
        }
        
    }
    
    return root;
    
}

int height(NODE node)
{
    if (node == NULL)
        return 0;
    else {
        int lheight = height(node->left);
        int rheight = height(node->right);
 
        if (lheight > rheight)
            return (lheight + 1);
        else
            return (rheight + 1);
    }
}

void printCurrentLevel(NODE root, int level)
{
    if (root == NULL)
        return;
    if (level == 1)
        printf("%d ", root->data);
    else if (level > 1) {
        printCurrentLevel(root->left, level - 1);
        printCurrentLevel(root->right, level - 1);
    }
}

void printLevelOrder(NODE root)
{
    int h = height(root);
    int i;
    for (i = 1; i <= h; i++){
        printCurrentLevel(root, i);
        printf("\n");
    }
}


int main(void){
	
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
    printf("\n");
    printLevelOrder(root);
    
	return 0;
}

