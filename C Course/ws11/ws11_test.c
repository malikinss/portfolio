/* 
Reviewed by ...
Contains tests of ws11 functions. 
Created by Sam 
*/

#include <stdio.h> /* printf() */
#include <stdlib.h> /* atoi() */
#include "ws11.h"

static int CompareAtoiWithLibrary(char string[]);
static int TestAtoi();

static void TestPrintCharsIn1And2Not3();
static void IfCompareData(int compare_data, int *result);
static void FastTestAtoiItoa();
static void TestFailed();
static void TestPassed();


int RunIsLittleEndianMacro();

int main()
{
    FastTestAtoiItoa();
    TestAtoi();
    TestPrintCharsIn1And2Not3();
    printf("IsLittleEndian? Using function: %s\n", 
        (IsLittleEndian()) ? "yes" : "no");
    printf("IsLittleEndian? Using macro: %s\n", 
        (RunIsLittleEndianMacro()) ? "yes" : "no");
   return 0;
}

static int CompareAtoiWithLibrary(char string[])
{
    return (atoi(string) == AtoiBase10(string));
}

static void TestPassed()
{
	printf("Test Passed\n");
}

static void TestFailed()
{
	printf("Test Failed\n");
}

static void IfCompareData(int compare_data, int *result)
{
	if(1 == compare_data)
    {
    	TestPassed();
    }
    else
    {
        TestFailed();
        *result += 1;                
    }
}

static int TestAtoi()
{
    int result = 0;
    int compare_data = 0;

    printf("Testing Atoi vs Library:\n");

    printf("Testing '123456'\n");
    compare_data = CompareAtoiWithLibrary("123456");
    IfCompareData(compare_data, &result);
    

    printf("Testing '0000'\n");
    compare_data = CompareAtoiWithLibrary("0000");
	IfCompareData(compare_data, &result);  

    printf("Testing '2147483647'\n");  
    compare_data = CompareAtoiWithLibrary("2147483647");
	IfCompareData(compare_data, &result);  

    printf("Testing '-2147483647'\n");  
    compare_data = CompareAtoiWithLibrary("-2147483647");
	IfCompareData(compare_data, &result);

    return result;
}

static void FastTestAtoiItoa()
{
    int num1 = 123456;
    int num2 = -1234;
    char buffer[10] = "000000000";
    char num3[] = "123456";
    char num4[] = "-1234";
    char num5[] = "2n9c";
    char num6[] = "-ya";

    printf("Testing ItoaBase10:\n");
    ItoaBase10(num1, buffer);
    printf("Converting from  %d\tto  '%s'\n", num1, buffer);
    ItoaBase10(num2, buffer);
    printf("Converting from  %d\tto  '%s'\n", num2, buffer);
    printf("-----------\n");

    printf("Testing AtoiBase10:\n");
    printf("Converting from  '%s'\tto  %d\n", num3, AtoiBase10(num3));
    printf("Converting from  '%s'\tto  %d\n", num4, AtoiBase10(num4));
    printf("-----------\n");

    printf("Testing ItoaBaseUp36:\n");
    ItoaBaseUp36(num1, 36, buffer);
    printf("Converting from  %d\tto  '%s'\n", num1, buffer);
    ItoaBaseUp36(num2, 36, buffer);
    printf("Converting from  %d\tto  '%s'\n", num2, buffer);
    printf("-----------\n");

    printf("Testing AtoiBaseUp36:\n");
    printf("Converting from  '%s'\tto  %d\n", num5, AtoiBaseUp36(num5, 36));
    printf("Converting from  '%s'\tto  %d\n", num6, AtoiBaseUp36(num6, 36));
    printf("-----------\n");   
}

static void TestPrintCharsIn1And2Not3()
{
    char chars1[5] = {'a', 'b', 'a', 'z', '/'};
    char chars2[5] = {'b', 'a', 'z', 'a', '/'};
    char chars3[5] = {'e', 'w', 'q', 'z', 'e'};
    size_t size1 = sizeof(chars1) / sizeof(chars1[0]);
    size_t size2 = sizeof(chars2) / sizeof(chars2[0]);
    size_t size3 = sizeof(chars3) / sizeof(chars3[0]);
    size_t i = 0;

    printf("Testing PrintCharsIn1And2Not3:\n");
    printf("chars1 = ");
    for(i = 0; i < size1; ++i)
    {
        printf("%c", chars1[i]);
    }

    printf("\nchars2 = ");
    for(i = 0; i < size2; ++i)
    {
        printf("%c", chars2[i]);
    }

    printf("\nchars3 = ");
    for(i = 0; i < size3; ++i)
    {
        printf("%c", chars3[i]);
    }

    printf("\nAnswer:  ");
    PrintCharsIn1And2Not3(chars1, size1, chars2, size2, chars3, size3);
    printf("-----------\n");
}
