/* 
	Reviewed by Maxim 
	Created by Sam
*/
#include <stdio.h>

#define MAX2(a, b) ((a) > (b) ? (a) : (b))
#define MAX3(a, b, c) ((a) > (b) ? (a > c ? a : c) : (b > c ? b : c))
#define SIZEOF_VAR(a) ((size_t)((&a)+1) - (size_t)&a)

#define SIZEOF_TYPE(a) ({a var; (SIZEOF_VAR(var));})

int main()
{
    char s = 'a';
    
    int a = 2;
    int b = 3;
    int c = 4;

    printf("Max of %d and %d is: %d\n", a, b ,MAX2(a, b));

    printf("Max of %d, %d and %d is: %d\n", a, b, c, MAX3(a, b, c));

    printf("size of variable s = %ld bytes\n", SIZEOF_VAR(s));
    printf("size of variable a = %ld bytes\n", SIZEOF_VAR(a));
    
    printf("size of type char =%ld bytes\n", SIZEOF_TYPE(char));
    printf("size of type int =%ld bytes\n", SIZEOF_TYPE(int));

    return 0;
}
