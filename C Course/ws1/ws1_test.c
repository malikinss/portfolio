#include <stdio.h> 		/* printf() */
#include <math.h> 		/* pow */
#include <stddef.h>
#include "ws1.h"

void TestPrintHelloWorld();
void TestPowOfTen(); 
void TestFlipNum();
void TestSwap();

int main()
{
	TestPrintHelloWorld();
	TestPowOfTen(); 
	TestFlipNum();
	TestSwap();

    return 0;
}



void PrintTestName(char *name)
{
	printf("******************************\n");
	printf("Test of %s\n", name);
	
}

void TestPrintHelloWorld()
{	
	PrintTestName("PrintHello");
	PrintHelloWorld();
}

void TestPowOfTen()
{
    double x = PowOfTen(2);
    double y = PowOfTen(-2);

    double xt = pow(10.0, 2);
    double yt = pow(10.0, -2);
    
	PrintTestName("PowOf10");

    if( 0.001 > (x - xt)  && 0.001 > (y - yt))
    {
        printf("Test Passed\n");
        printf("******************************\n");
    }
    else
    {
        printf("Test Failed\n");
        printf("******************************\n");
    }
}

void TestFlipNum()
{
	int a = -4031;
	int b = -1304;

	int a_test = FlipNum(a);
	int b_test = FlipNum(b);

	PrintTestName("FlipNum");

	if(a_test == b && b_test == a)
	{
		printf("Test Passed\n");
		printf("******************************\n");
	}
	else
	{
		printf("Test Failed\n");
		printf("******************************\n");
	}
}

void TestSwap()
{
    int a = 10;
    int b = 5;
    int c = 2;
    int d = 4;

    PrintTestName("Swap");

    Swap(&a, &b);
    Swap(&c, &b);
    Swap(&a, &d);

    if(4 == a && 2 == b && 10 == c && 5 == d)
    {
        printf("Test Passed\n");
        printf("******************************\n");
    }
    else
    {
        printf("Test Failed\n");
        printf("******************************\n");
    }
}
