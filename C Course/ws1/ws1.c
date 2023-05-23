#include <stdio.h> 		/* printf() puts() */
#include <assert.h> 	/* assert() */
#include <math.h> 		/* pow() */
#include <assert.h>		/* assert() */
#include <stddef.h>
#include "ws1.h"

void PrintHelloWorld()
{
	char hello_world[] = {0x22, 0x48, 0x65, 0x6C, 0x6C, 0x6F, 
        0x20, 0x57, 0x6F, 0x72, 0x6C, 0x64, 0x21, 0x22};
	printf("%s\n", hello_world);
}

double PowOfTen(int n)
{   
    float base = 10.0;
    double result = 1.0;
    int i = 0;
        
    assert(100 > n);
        
    if (0 > n)
    {
        base = 1 / base;
        n = -n;
    }
        
    for (i = 0; i < n; ++i)
    {
        result *= base;
    }
        
    return result;        
}

int FlipNum(int n)
{
	int result = 0;
	int last_digit = 0;
	int sign = 1;

	assert(NULL != n);
	
	if (n < 0)
	{
		n = -n;
		sign = -1;
	}

	while(0 != n)
	{
		last_digit = n % 10;
		result = result * 10 + last_digit;
		n = n / 10;
	}

	return result*sign;
}

void Swap(int *a, int *b)
{
    int tmp;

    assert(NULL != a);
    assert(NULL != b);
    
    tmp = *a;
    *a = *b;
    *b = tmp;
}

