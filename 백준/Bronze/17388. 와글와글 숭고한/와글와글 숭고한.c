#include <stdio.h>
#include <stdlib.h>

int main()
{
    int s,k,h,a;
    scanf("%d %d %d",&s,&k,&h);
    a = s+k+h;
    if(a >= 100){
        printf("OK");
    }
    else if(s<k && s<h){
        printf("Soongsil");
    }
    else if(k<s && k<h){
        printf("Korea");
    }
    else if(h<s && h<k){
        printf("Hanyang");
    }
}
