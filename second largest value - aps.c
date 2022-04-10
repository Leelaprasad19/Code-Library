#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

struct data{
    char str[80];
};
typedef struct data Data;

int lcur;

int isString(char str[]){
    
    int len = strlen(str),dots=0;
    lcur = len;
    
    for(int i=0;i<len;i++){
        if(isalpha(str[i]) || (!isdigit(str[i]) && str[i]!='.' && str[i]!='-')){
            return 1;
        }else if(str[i]=='.'){
            lcur = i;
            dots++;
        }
    }
    
    if(dots > 1){
        return 1; // String
    }else if(dots==1){
        return 2; // Float
    }else{
        return 3; // Int
    }
}

int main(){
    
    long long int i,n,imax1=-999999999999999999,imax2=-999999999999999999,fcount=0;
    
    int dcur;
    
    Data temp,smax1,smax2;
    
    strcpy(smax1.str,"");
    strcpy(smax2.str,"");
    
    scanf("%lld",&n);
    
    for(i=0;i<n;i++){
        
        scanf("%s",temp.str);
        
        dcur = isString(temp.str);
        
        if(dcur==2){
            fcount++;
        }
        
            
        if(strcmp(temp.str,smax1.str) > 0)
        {
            strcpy(smax2.str,smax1.str);   
            strcpy(smax1.str,temp.str);
        }
        else if(strcmp(temp.str,smax2.str) > 0 && strcmp(temp.str,smax1.str) < 0)
        {
            strcpy(smax2.str,temp.str);
        }
        
        if(dcur == 3){
            
            long long int temp__ = atoll(temp.str);
            
            if(temp__ > imax1)
            {
                imax2 = imax1;
                imax1 = temp__;
            }
            else if(temp__ > imax2 && temp__ < imax1)
            {
                imax2 = temp__;
            }
            
        }
        
    }
    
    
    if(strlen(smax2.str)!=0 && fcount > 0){
        printf("%s",smax2.str);
    }else if(imax2!=-999999999999999999){
            printf("%lld",imax2);
    }else{
        
        if(strlen(smax2.str)!=0){
            printf("%s",smax2.str);
        }else{
            printf("-1");
        }
        
    }
    
    
    return 0;
}