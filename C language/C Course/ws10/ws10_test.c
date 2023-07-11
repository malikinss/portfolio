/*  
	Reviewed by Sergey
	Contains tests for Memset(), Memcpy() and Memmove functions (from ws10).
	Created by Sam 
*/

#include <stdio.h> 	/*printf()*/
#include <string.h>	/*memset(), memcpy(), memmove()*/
#include "ws10.h"

static int TestMemset();
static int TestMemcpy();
static int TestMemmove();

int main()
{
	char good[7] = "passed";
	char bad[7] = "failed";

	printf("TestMemcpy %s\n", (!TestMemset()) ? good : bad);
	printf("TestMemcpy %s\n", (!TestMemcpy()) ? good : bad);
	printf("TestMemmove %s\n", (!TestMemmove()) ? good : bad);

	return 0;
}

static int TestMemset()
{
	char str1_1[32] = "1234567890123456789012345678901";
	char str2_1[32] = "1234567890123456789012345678901";
	char str1_2[6] = "12345";
	char str2_2[6] = "12345";
	int c_1 = 99;
	int c_2 = 108;
	int result = 0;

	printf("Start TestMemset:\n");

	memset(str1_1, c_1, 31);
	Memset(str2_1, c_1, 31);

	printf("str1_1 = %s\n", str1_1);
	printf("str2_1 = %s\n", str2_1);
	result += strcmp(str1_1, str2_1);

	memset(str1_2, c_2, 5);
	Memset(str2_2, c_2, 5);

	printf("str1_2 = %s\n", str1_2);
	printf("str2_2 = %s\n", str2_2);
	result += strcmp(str1_2, str2_2);

	return result;
}




static int TestMemcpy()
{
	char str1_1[32] = "1234567890123456789012345678901";
	char str2_1[32] = {0};
	char str3_1[32] = {0};
	char str1_2[6] = "12345";
	char str2_2[6] = {0};
	char str3_2[6] = {0};
	int result = 0;

	printf("Start TestMemcpy:\n");

	memcpy(str2_1, str1_1, 32);
	Memcpy(str3_1, str1_1, 32);

	printf("str2_1 = %s\n", str2_1);
	printf("str3_1 = %s\n", str3_1);
	result += strcmp(str2_1, str3_1);

	memcpy(str2_2, str1_2, 6);
	Memcpy(str3_2, str1_2, 6);

	printf("str2_2 = %s\n", str2_2);
	printf("str3_2 = %s\n", str3_2);
	result += strcmp(str2_2, str3_2);

	return result;
}

static int TestMemmove()
{
	char str1_1[32] = "1234567890123456789012345678901";
	char str2_1[32] = "1234567890123456789012345678901";
	char *src1_1 = str1_1;
	char *dest1_1 = str1_1 + 5;
	char *src2_1 = str2_1;
	char *dest2_1 = str2_1 + 5;	
	char str1_2[32] = "1234567890123456789012345678901";
	char str2_2[32] = "1234567890123456789012345678901";
	char *src1_2 = str1_2 + 5;
	char *dest1_2 = str1_2;
	char *src2_2 = str2_2 + 5;
	char *dest2_2 = str2_2;
	int result = 0;

	printf("Start TestMemmove:\n");

	memmove(dest1_1, src1_1, 20);
	Memmove(dest2_1, src2_1, 20);

	printf("dest1_1 = %s\n", dest1_1);
	printf("dest2_1 = %s\n", dest2_1);
	result += strcmp(dest1_1, dest2_1);

	memmove(dest1_2, src1_2, 20);
	Memmove(dest2_2, src2_2, 20);

	printf("dest1_2 = %s\n", dest1_2);
	printf("dest2_2 = %s\n", dest2_2);
	result += strcmp(dest1_2, dest2_2);

	return result;
}
