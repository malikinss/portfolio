/*

Rewieved by 
Created by Sam

*/
#include <stdio.h> /* prinf() */

#include "bitarray.h"

#define START_VALUE (0xF00FF000F0000FFF)
#define ROTATE_LEFT_VALUE (0xF800780007FFF807)
#define ROTATE_RIGHT_VALUE (0x1FFFE01FE001E000)
#define MIRROR_VALUE (0xFFF0000F000FF00F)
#define SET_64_BIT (0xFFFFFFFFFFFFFFFF)
#define RESET_64_BIT (0x0)



int TestBitArrayResetAll(bitsarr_t bit_array);
int TestBitArraySetAll(bitsarr_t bit_array);
int TestBitArraySetOn(bitsarr_t bit_array);
int TestBitArraySetOff(bitsarr_t bit_array);
int TestBitArraySetBit(bitsarr_t bit_array);
int TestBitArrayGetVal(bitsarr_t bit_array);
int TestBitArrayFlip(bitsarr_t bit_array);
int TestBitArrayMirror(bitsarr_t bit_array);
int TestBitArrayRotateLeft(bitsarr_t bit_array);
int TestBitArrayRotateRight(bitsarr_t bit_array);
int TestBitArrayCountOn(bitsarr_t bit_array);
int TestBitArrayCountOff(bitsarr_t bit_array);
int TestBitArrayToString(bitsarr_t bit_array);
int TestBitArrayCountOnLUT(bitsarr_t bit_array);
int TestBitArrayMirrorLUT(bitsarr_t bit_array);

int main()
{
	bitsarr_t bit_array = 0;
	
	
	TestBitArraySetAll(bit_array);
	TestBitArrayResetAll(bit_array);
	TestBitArraySetOn(bit_array);
	TestBitArraySetOff(bit_array);
	TestBitArrayGetVal(bit_array);
	TestBitArraySetBit(bit_array);
	TestBitArrayFlip(bit_array);
	TestBitArrayMirror(bit_array);
	TestBitArrayRotateRight(bit_array);
	TestBitArrayRotateLeft(bit_array);
	TestBitArrayCountOn(bit_array);
	TestBitArrayCountOnLUT(bit_array);
	TestBitArrayCountOff(bit_array);
	TestBitArrayToString(bit_array);
	TestBitArrayMirrorLUT(bit_array);
	
	return (0);
}

void TestPassed(char *name)
{
	printf("\n");
	printf("Test for %s passed\n", name);
	printf("**********************\n");
}

void TestFailed(char *name)
{
	printf("\n");
	printf("Test for %s Failed\n", name);
	printf("**********************\n");
}

int PrintString(bitsarr_t bit_array)
{
	char any_string[65] = {0};
	BitArrayToString(bit_array, any_string);
	printf("%s\n", any_string);
	return 0;
}

int IfForAllTestsArr(bitsarr_t bit_array, char *name, bitsarr_t test_value)
{
	if(test_value == bit_array)
	{
		TestPassed(name);
		return 1;
	}
	TestFailed(name);
	return 0;
}

int IfForAllTestsBits(int bit_value, char *name, int test_value)
{
	if(test_value == bit_value)
	{
		TestPassed(name);
		return 1;
	}
	TestFailed(name);
	return 0;
}

int TestBitArraySetAll(bitsarr_t bit_array)
{
	bit_array = BitArraySetAll(bit_array);
	return IfForAllTestsArr(bit_array, "SetAll", SET_64_BIT);
}

int TestBitArrayResetAll(bitsarr_t bit_array)
{
	bit_array = BitArrayResetAll(bit_array);
	return IfForAllTestsArr(bit_array, "ResetAll", RESET_64_BIT);
}

int TestBitArraySetOn(bitsarr_t bit_array)
{
	int bit_value = 0;
	bit_array = BitArraySetOn(bit_array, 0);
	bit_value = BitArrayGetVal(bit_array, 0);
	return IfForAllTestsBits(bit_value, "SetOn", 1);
}

int TestBitArraySetOff(bitsarr_t bit_array)
{
	int bit_value = 0;
	bit_array = BitArraySetAll(bit_array);	
	bit_array = BitArraySetOff(bit_array, 7);
	bit_value = BitArrayGetVal(bit_array, 7);
	return IfForAllTestsBits(bit_value, "SetOff", 0);
}

int TestBitArraySetBit(bitsarr_t bit_array)
{
	int bit_value = 0;
	bit_array = BitArraySetAll(bit_array);
	bit_array = BitArraySetBit(bit_array, 1, 0);
	bit_value = BitArrayGetVal(bit_array, 1);
	return IfForAllTestsBits(bit_value, "SetBit", 0);
}

int TestBitArrayFlip(bitsarr_t bit_array)
{
	int bit_value = 0;
	bit_array = BitArraySetBit(bit_array, 7, 0);
	bit_array = BitArrayFlip(bit_array, 7);
	bit_value = BitArrayGetVal(bit_array, 7);
	return IfForAllTestsBits(bit_value, "Flip", 1);
}

int TestBitArrayGetVal(bitsarr_t bit_array)
{
	int bit_value = 0;
	bit_array = BitArraySetAll(bit_array);	
	bit_value = BitArrayGetVal(bit_array, 7);
	return IfForAllTestsBits(bit_value, "GetVal", 1);
}

int TestBitArrayMirror(bitsarr_t bit_array)
{
	bit_array = BitArrayResetAll(bit_array);
	bit_array = bit_array | START_VALUE;
	bit_array = BitArrayMirror(bit_array);
	return IfForAllTestsArr(bit_array, "MIRROR", MIRROR_VALUE);
}

int TestBitArrayRotateLeft(bitsarr_t bit_array)
{
	bit_array = BitArrayResetAll(bit_array);
	bit_array = bit_array | START_VALUE;
	bit_array = BitArrayRotateLeft(bit_array, 15);
	return IfForAllTestsArr(bit_array, "RotateLeft", ROTATE_LEFT_VALUE);
}


int TestBitArrayRotateRight(bitsarr_t bit_array)
{
	bit_array = BitArrayResetAll(bit_array);
	bit_array = bit_array | START_VALUE;
	bit_array = BitArrayRotateRight(bit_array, 15);
	return IfForAllTestsArr(bit_array, "RotateRight", ROTATE_RIGHT_VALUE);
}

int TestBitArrayCountOn(bitsarr_t bit_array)
{
	bit_array = BitArrayResetAll(bit_array);
	bit_array = bit_array | START_VALUE;
	bit_array = BitArrayCountOn(bit_array);
	return IfForAllTestsArr(bit_array, "CountOn", 28);
}

int TestBitArrayCountOnLUT(bitsarr_t bit_array)
{
	bit_array = BitArrayResetAll(bit_array);
	bit_array = bit_array | START_VALUE;
	bit_array = BitArrayCountOnLUT(bit_array);
	return IfForAllTestsArr(bit_array, "CountOnLUT", 28);
}

int TestBitArrayCountOff(bitsarr_t bit_array)
{
	bit_array = BitArrayResetAll(bit_array);
	bit_array = bit_array | START_VALUE;
	bit_array = BitArrayCountOff(bit_array);
	return IfForAllTestsArr(bit_array, "CountOff", 36);
}

int TestBitArrayToString(bitsarr_t bit_array)
{
	bit_array = BitArrayResetAll(bit_array);
	PrintString(bit_array);
	bit_array = bit_array | START_VALUE;
	PrintString(bit_array);
	return 0;
}

int TestBitArrayMirrorLUT(bitsarr_t bit_array)
{	
	
	bit_array = BitArrayResetAll(bit_array);
	bit_array = bit_array | START_VALUE;
	PrintString(bit_array);
	
	bit_array = BitArrayMirrorLUT(bit_array);
	PrintString(bit_array);
	
	return IfForAllTestsArr(bit_array, "MirrorLUT", MIRROR_VALUE);
}
