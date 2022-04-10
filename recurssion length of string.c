#include<stdio.h>
#include<stdlib.h>
int LenStr(char* str)
{
    if (*str == '\0')
        return 0;
    else
        return 1 + LenStr(str + 1);
}

int main()
{
    int len;
    char str[20];
    scanf("%s",str);
    len= LenStr(str);
    printf("Length of the string = %d",len);
    return 0;
}
