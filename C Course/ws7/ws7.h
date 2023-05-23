/*	
	Reviewed by Allan
	Contains definition different bitwise functions. 
	Created by Sam 
*/
#ifndef __WS7_H__
#define __WS7_H__

#include <stddef.h> /* size_t */

/*DESCRIPTION 
Function calculates the result of x*(2^y);

RETURN 
The result of calculation.

PARAMS
x: an usigned int number
y: an usigned int number
*/
long Pow2(unsigned int x, unsigned int y);

/*
DESCRIPTION 
- Function checks if the given number is a power of 2.
- IsPowerOf2V1 does assessment using a loop.
- IsPowerOf2V2 does assessment without using a loop.

RETURN
1 if the number is a power of 2. 
0 if it isn't.

PARAMS
n: an unsigned int number.
*/
int IsPowerOf2V1(unsigned int n);
int IsPowerOf2V2(unsigned int n);

/* 
DESCRIPTION
- Increments an interger number passed to it.
- Does not use arithmetic operators.

RETURN
New value of the number.

PARAMS
n: an int number.
*/
int AddOne(int n);


/* 
DESCRIPTION
- Function goes through an array of unsigned ints.
- Prints only numbers that have 3 bits set to 1 (for ex, 7, 11, 14, etc.).

RETURN
Function doesn't return anyrthing.

PARAMS
arr: array of unsigned ints
size: size of the array
*/
void PrintNumsWithThreeBitsOn (unsigned int *arr, size_t size);

/*
DESCRIPTION
- Function receives an unsigned char and reverses its bits.
(for ex., 00000101 becomes 10100000)
- ByteMirrorV1 does that using a loop.
- ByteMirrorV2 doesn't use a loop.

RETURN
Function returns the new char.

PARAMS
c: an unsigned char
*/
unsigned char ByteMirrorV1(unsigned char c);
unsigned char ByteMirrorV2(unsigned char c);

/*
DESCRIPTION
- Function receives an unsigned char.
- Checks if thr 2nd and 6th bits are set to 1. 

RETURN
1 if both bits are set to 1.
0 if either of the bits is not set to 1.

PARAMS
c: an unsigned char
*/
int Is2ndAnd6thOn(unsigned char c);

/*
DESCRIPTION
- Function receives an unsigned char.
- Checks if the 2nd and 6th bits are set to 1. 

RETURN
1 if either of the bits is set to 1.
0 if both bits are not set to 1.

PARAMS
c: an unsigned char
*/
int Is2ndOr6thOn(unsigned char c);

/*
DESCRIPTION
- Function receives an unsigned char.
- Swaps the 3nd and the 5th bits. 

RETURN
an unsigned char resulting from the bit swap;

PARAMS
c: an unsigned char
*/
unsigned char Swap3rdAnd5th(unsigned char c);

/* 
DESCRIPTION
- Recives an usigned number n 
- Finds the closest to n smaller number that is divisible by 16 without 
a reminder.
(Ex: 32 for 33, 16 for 22)

RETURN
The found number.

PARAMS
n: an unsigned int number.
*/
unsigned int ClosestDivisibleBy16(unsigned int n);

/*
DESCRIPTION
- Function recieves pointers to two integers.
- Swaps two integers.
- Doesn't use a temp.
- Doesn't work if both pointers are equal (point at the same location). 

RETURN
0 if the swap is succesful
-1 if pointers  are equal.

PARAMS
n1: a pointer to an integer.
n1: a pointer to an integer.
*/
void SwapWithoutTemp(int *n1, int *n2);

/* 
DESCRIPTION
Function counts the number of set bits in an integer.
V1 is using a loop.
V2 isn't using a loop.'


RETURN
function return number of set bits 

PARAMS
num: number from where to count sets
*/
size_t SetBitsCountV1(int num);
size_t SetBitsCountV2(int num);

/* 
DESCRIPTION
- Function that receives a float from the user, and prints its bits

RETURN
Function doesn't return anything.

PARAMS
user_input: float number
*/
void FloatAnalysis(float user_input);

#endif /* __WS7_H__ */
