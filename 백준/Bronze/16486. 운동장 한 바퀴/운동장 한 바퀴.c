#include <stdio.h>

int main(){
    int a, b;
    float pi = 3.141592;
    scanf("%d %d", &a, &b);
    printf("%f", (float)a*2 + 2*pi*(float)b);
    return 0;
}