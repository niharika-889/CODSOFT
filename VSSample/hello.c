
#include <stdio.h>
int num=11;
void show(){
    printf("%d",num);
}
int main(){
    show();
    printf("%d",num);
    num=13;
    show();
    return 0;

}