/*	
	Reviewed by Allan
	Contains test functions for bitwise functions from ws7.c. 
	Created by Sam 
*/

#include <stdio.h>		/* printf */
#include <math.h>		/* pow */
#include <assert.h> 	/* assert*/
#include <stddef.h> 	/* size_t*/

#include "ws7.h"

#define MASK_6AND2 (68)

void TestPow2();
void TestIsPowOf2V1();
void TestIsPowOf2V2();
void TestAddOne();
void TestPrintNumsWithThreeBitsOn();
void TestByteMirrorV1();
void TestByteMirrorV2();
void TestIs2ndAnd6thOn();
void TestIs2ndOr6thOn();
void TestSwap3rdAnd5th();
void TestClosestDivisibleBy16();
void TestSwapWithoutTemp();
void TestSetBitsCountV1();
void TestSetBitsCountV2();
void Test10();

int main()
{	
	TestPow2();
	TestIsPowOf2V1();	
	TestIsPowOf2V2();
	TestAddOne();
	TestPrintNumsWithThreeBitsOn();
	TestByteMirrorV1();
	TestByteMirrorV2();
	TestIs2ndAnd6thOn();
	TestIs2ndOr6thOn();
	TestSwap3rdAnd5th();
	TestClosestDivisibleBy16();
	TestSwapWithoutTemp();
	TestSetBitsCountV1();
	TestSetBitsCountV2();
	Test10();		
	return 0;
}

void TestResult(const int expression, const char *func_name)
{
	if(expression)
	{
		printf("Test %s Passed\n", func_name);
	}
	else
	{
		printf("Test %s Failed\n", func_name);
	}
}

void TestPow2()
{
	const char func_name[] = "Pow2";
	
	unsigned int a = 3;
	unsigned int b = 4;
	
	unsigned int x = 2;
	
	long my_func_ret = 0;
	long std_func_ret = 0;
	int expression = 0; 
	
	my_func_ret = Pow2(a, b);
	std_func_ret =  a*(pow(x,b));
	
	expression = (my_func_ret == std_func_ret);
	
	TestResult(expression, func_name);
	
}

void TestIsPowOf2V1()
{
	const char func_name[] = "IsPowOf2V1";
	
	const unsigned int n = 16;
	const int ispowof2 = 1;
	
	int my_func_ret = 0;
	int std_func_ret = 0;
	int expression = 0;	 
	
	my_func_ret = IsPowerOf2V1(n);
	std_func_ret = ispowof2;
	expression = (my_func_ret == std_func_ret);

	TestResult(expression, func_name);
}

void TestIsPowOf2V2()
{
	const char func_name[] = "IsPowOf2V2";
	
	const unsigned int n = 32;
	const int ispowof2 = 1;
	
	int my_func_ret = 0;
	int std_func_ret = 0;
	int expression = 0;	 
	
	my_func_ret = IsPowerOf2V2(n);
	std_func_ret = ispowof2;
	expression = (my_func_ret == std_func_ret);

	TestResult(expression, func_name);
}

void TestAddOne()
{
	const char func_name[] = "AddOne";
	
	int n = 7;
	int my_func_ret = 0;
	int std_func_ret = 0;
	int expression = 0; 
	
	my_func_ret = AddOne(n);
	std_func_ret = n+1;
	expression = (my_func_ret == std_func_ret);
	
	TestResult(expression, func_name);
}

void TestPrintNumsWithThreeBitsOn()
{
	unsigned int test_arr [14]= {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14};
	PrintNumsWithThreeBitsOn(test_arr, 14);
}

void TestByteMirrorV1()
{
	const char func_name[] = "ByteMirrorV1";
	
	unsigned char c = 10;
	
	unsigned char my_func_ret = 0;
	unsigned char std_func_ret = 0;
	
	int expression = 0; 
	
	my_func_ret = ByteMirrorV1(c);
	std_func_ret = ByteMirrorV2(c);
	
	expression = (my_func_ret == std_func_ret);
	
	TestResult(expression, func_name);	
}

void TestByteMirrorV2()
{
	const char func_name[] = "ByteMirrorV2";
	
	unsigned char c = 10;
	
	unsigned char my_func_ret = 0;
	unsigned char std_func_ret = 0;
	
	int expression = 0; 
	
	my_func_ret = ByteMirrorV2(c);
	std_func_ret = ByteMirrorV1(c);
	
	expression = (my_func_ret == std_func_ret);
	
	TestResult(expression, func_name);	
}

void TestIs2ndAnd6thOn()
{	
	const char func_name[] = "Is2ndAnd6thOn";
	
	unsigned char c = 87;
	
	int my_func_ret = 0;
	int std_func_ret = 0;
	int expression = 0; 
	
	my_func_ret = Is2ndAnd6thOn(c);
	std_func_ret = Is2ndAnd6thOn(MASK_6AND2);
	
	expression = (my_func_ret == std_func_ret);
	
	TestResult(expression, func_name);	
}

void TestIs2ndOr6thOn()
{	
	const char func_name[] = "Is2ndOr6thOn";
	
	unsigned char c = 64;
	
	int my_func_ret = 0;
	int std_func_ret = 0;
	int expression = 0; 
	
	my_func_ret = Is2ndOr6thOn(c);
	std_func_ret = Is2ndOr6thOn(MASK_6AND2);
	
	expression = (my_func_ret == std_func_ret);
	
	TestResult(expression, func_name);	
}

void TestSwap3rdAnd5th()
{
	const char func_name[] = "Swap3rdAnd5th";
	
	unsigned char c = 8;
	unsigned char my_func_ret = 0;
	unsigned char std_func_ret = 32;
	int expression = 0; 
	
	my_func_ret = Swap3rdAnd5th(c);
	
	expression = (my_func_ret == std_func_ret);
	
	TestResult(expression, func_name);
}

void TestClosestDivisibleBy16()
{	
	const char func_name[] = "ClosestDivisibleBy16";
	
	unsigned int n = 33;
	unsigned int my_func_ret = 0;
	unsigned int std_func_ret = 32;
	int expression = 0; 
	
	my_func_ret = ClosestDivisibleBy16(n);
	
	expression = (my_func_ret == std_func_ret);
	
	TestResult(expression, func_name);
}

void TestSwapWithoutTemp()
{
	const char func_name[] = "SwapWithoutTemp";
	
	int a = 5;
	int b = 4;
	
	int expression = 0; 
	
	SwapWithoutTemp(&a, &b);
	SwapWithoutTemp(&a, &b);
	
	expression = (5 == a && 4 == b);
	
	TestResult(expression, func_name);
}

void TestSetBitsCountV1()
{	
	const char func_name[] = "SetBitsCountV1";
	
	int num = 5;
	size_t my_func_ret = 0;
	size_t total = 2;
	
	int expression = 0; 
	
	my_func_ret = SetBitsCountV1(num);
	
	expression = (my_func_ret == total);
	
	TestResult(expression, func_name);
}

void TestSetBitsCountV2()
{	
	const char func_name[] = "SetBitsCountV2";
	
	int num = 5;
	size_t my_func_ret = 0;
	size_t total = 2;
	
	int expression = 0; 
	
	my_func_ret = SetBitsCountV2(num);
	
	expression = (my_func_ret == total);
	
	TestResult(expression, func_name);
}

void Test10()
{
	
	FloatAnalysis(4.1);
}
