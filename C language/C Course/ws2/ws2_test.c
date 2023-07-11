#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include "ws2.h"

void TestStrCmp();
void TestStrLen();
void TestCopyIntArray();
void TestSwap();


int main()
{
    TestSwap();
    printf("\n");
    
    TestCopyIntArray();
    printf("\n");
    
    TestStrLen();
    printf("\n");
    
    TestStrCmp();
    printf("\n");
    
    return 0;
}

/******************** Test of Swap Functions ************************/
void TestSwap()
{	
    int a = 1;
    int b = 5;
    
    int test_a = a;
    int test_b = b;
    	
    size_t first = 4;
    size_t second = 8;
    
    size_t test_f = first;
    size_t test_s = second;
    
    
    size_t *firstp = &first;
    size_t *secondp = &second;
    
    size_t *test_fp = firstp;
    size_t *test_sp = secondp;
    
    
    size_t **firstpp = &firstp;
    size_t **secondpp = &secondp;
    
    printf("Testing Swap\n");
    Swap(&a, &b);
    
    if (test_b == a && test_a == b)
    {
        printf("Pass\n");
    }
    else
    {
        printf("Fail\n");
    }
    
    printf("Testing SwapSizeT\n");
    SwapSizeT(firstp, secondp);
    
    if (test_f == second && test_s == first)
    {
        printf("Pass\n");
    }
    else
    {
        printf("Fail\n");
    }
    
    printf("Testing SwapSizeTPtr1\n");
    SwapSizeTPtr1(firstpp, secondpp);
    
    if (test_sp == firstp && test_fp == secondp)
    {
        printf("Pass\n");
    }
    else
    {
        printf("Fail\n");
    }
    
    printf("Testing SwapSizeTPtr2\n");
    SwapSizeTPtr2(firstpp, secondpp);
    SwapSizeTPtr2(firstpp, secondpp);
    
    if (test_sp == firstp && test_fp == secondp)
    {
        printf("Pass\n");
    }
    else
    {
        printf("Fail\n");
    }
}

/******************** Test of Array Copy ************************/
void TestCopyIntArray()
{
    int arr1[] = {1, 2, 3, 4, 5};
    int arr2[] = {1};
    int new_array[5];
    int new_array2[1];
    CopyIntArray(arr1, new_array, sizeof(arr1));

    printf("Testing ArrayCopy***\n");

    if (memcmp(arr1, new_array, sizeof(arr1)) == 0)
    {
        printf("Pass\n");
    }
    else
    {
        printf("Fail\n");
    }

    CopyIntArray(arr2, new_array2, sizeof(arr2));

    if (memcmp(arr2, new_array2, sizeof(arr2)) == 0)
    {
        printf("Pass\n");
    }
    else
    {
        printf("Fail\n");
    }
}

/******************** Test of LenStr ************************/

void TestStrLen()
{
    char str1[] = "Sam";
    char str2[] = " the ";
    char str3[] = "Best!!!";
        
    int test_len1 = StrLen(str1);
    int test_len2 = StrLen(str2);
    int test_len3 = StrLen(str3);
        
    int tl1 = strlen(str1);
    int tl2 = strlen(str2);
    int tl3 = strlen(str3);
    
    printf("Testing function LenStr\n");
        
    if(tl1 == test_len1 && tl2 == test_len2 && tl3 == test_len3)
    {
        printf("All tests passed succesfully!\n");
    }
    else
    {
        printf("testing error!");
    }
}

/******************** Test of StrCmp ************************/

void TestStrCmp()
{
    char first_str[] = "Sam";
    char second_str[] = "Sam";
    char third_str[] = "Sam!";
    char fourth_str[] = "Sm";
        
    int strcmp_t1 = strcmp(first_str, second_str);
    int strcmp_t2 = strcmp(second_str, third_str);
    int strcmp_t3 = strcmp(third_str, fourth_str);
        
    int test_cmp1 = StrCmp(first_str, second_str);
    int test_cmp2 = StrCmp(second_str, third_str);
    int test_cmp3 = StrCmp(third_str, fourth_str);
    
    printf("Testing function StrCmp\n");
    
    if(strcmp_t1 == test_cmp1 && strcmp_t2 == test_cmp2 && strcmp_t3 == test_cmp3)
    {
        printf("Tests passed");
    }
    else
    {
        printf("Tests failed");
    }
}
