/* 
Reviewed by Michael 
Header file, contains description of ItoaBase10(), AtoiBase10(), 
ItoaBaseUp36(), AtoiBaseUp36(), PrintCharsIn1And2Not3() and IsLittleEndian()
functions. Function definitions in the ws_11.c file. 
Created by Sam 
*/
#ifndef __WS11_H__
#define __WS11_H__

#include <stddef.h> /* size_t */

/*
DESCRIPTION
- Function converts int to dest string base of 10, 
    user should make sure that dest is big enough to fit number

RETURN
- Function doesnt return anything

INPUT
- num: input number;
- dest: destination string
*/
void ItoaBase10(int num, char *dest);  


/*
DESCRIPTION
- Function converts string base of 10 to int, 
    user should make sure string is small enough to fit the range of int 32-bit

RETURN
- Function return int number 

INPUT
- src: source string
*/
int AtoiBase10(const char *src); 


/*
DESCRIPTION
- Function converts int to dest string base of 36, user should make sure
    that dest string in big enough to fit number

RETURN
- Function doesnt return anything

INPUT
- desr: dest string
- num: number to convert from
- base: base
*/
void ItoaBaseUp36(int num, size_t base, char *dest);  


/*
DESCRIPTION
- Function converts string up to base 36 to int, user should make sure
    string representation of number is in size of INT values.

RETURN
- Function return int number

INPUT
- src: source string
- base: base
*/
int AtoiBaseUp36(const char *src, size_t base);  


/*
DESCRIPTION
- The function recieves 3 arrays of chars.
- Prints characters that appear in both arrays 1 and 2 but don't appear 
    in the array 3.
- Every character is printed only once.
- The function loops through each array once.  

RETURN
The function doesn't return anything.

INPUT
chars1: an array of chars;
chars2: an array of chars;
chars3: an array of chars.
*/
void PrintCharsIn1And2Not3(char chars1[], size_t size1, char chars2[], 
    size_t size2, char chars3[], size_t size3);                                                   


/*
DESCRIPTION
The function checks if the computer it's run on is little-endian.

RETURN
1 - if the computer is little-endian.
0 - if the computer is not little-endian.

INPUT
The function has no input.
*/
int IsLittleEndian(); 


#endif /* __WS11_H__ */

