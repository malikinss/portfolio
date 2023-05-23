/*	
	Reviewed by Allan
	Contains implementation different bitwise functions. 
	Created by Sam 
*/
#include <stdio.h>		/* printf */  
#include <assert.h> 	/* assert*/
#include <stddef.h> 	/* size_t*/

#include "ws7.h"

#define MASK_6AND2 (68)
#define BYTE_LENGTH (7)

#define DIV_BY_16 (~(0xF))

#define LEFT_NIBL (0xF0)
#define RIGHT_NIBL (0x0F)

#define LEFT_PAIR (0xCC)
#define RIGHT_PAIR (0x33)

#define LEFT_ONES (0xAA)
#define RIGHT_ONES (0x55)

#define MASK_BIT (0x1)

#define MASK_ONES (0x55555555)
#define MASK_PAIR (0x33333333)
#define MASK_NIBL (0x0F0F0F0F)
#define MASK_BYTE (0x00FF00FF)
#define MASK_HALF (0xFFFF)


#define ZERO (0)

long Pow2(unsigned int x, unsigned int y)
{
    return ((long)(x << y));
}

int IsPowerOf2V1(unsigned int n)
{
    unsigned int i = 0;
    unsigned int x = 2;
    
    if(0 == n)
    {
    	return (1);
    }
                                            
    for(i = 0; n >= i; ++i)
    {
        x =  x << 1;
        if(x == n)
        {
            return (1);
        }
    }
    return (0);
}

int IsPowerOf2V2(unsigned int n)
{
    return ((0 != n) && (0 == (n & (n - 1))));
}

int AddOne(int n)
{
    int mask = MASK_BIT;

	assert(0 != n);                   
	
    while (n & mask)                            
    {
        n = n ^ mask;
        mask = mask << 1;
    }

    return (n ^ mask);
}

size_t CountBits(unsigned int n)
{
	size_t counter = 0;
	size_t i = 0;
	
	assert(0 != n);                   
	
	for ( i = 0; i < 32; ++i)
    {
    	if (n & 1)
        {                               
        	++counter;
		}
		n = n >> 1;
    }
	return (counter);
}

void PrintNumsWithThreeBitsOn (unsigned int *arr, size_t size)
{
    size_t i = 0;
    
    assert(NULL != arr);
    assert(0 != size);      
    
    printf("\n");
    for ( i = 0; i < size; ++i)
    {   
        if(3 == CountBits(arr[i]))
        {
            printf("PrintNumsWithThreeBitsOn : %u\n", arr[i]);
        }
    }
    printf("\n");
}

unsigned char ByteMirrorV1(unsigned char c)
{
    unsigned char reverse = 0;
    unsigned char result = c;
    size_t i = 0;
    
    for(i = 0; BYTE_LENGTH > i; ++i)
    {
		reverse <<= 1;
        if (result & 1)                 
        {
            reverse ^= 1;
        }
        result >>= 1;    
    }
    reverse <<= 1;           
    return (reverse);
}

unsigned char ByteMirrorV2(unsigned char c)
{	
    c = ((c & LEFT_NIBL ) >> 4 | (c & RIGHT_NIBL) << 4);
    c = ((c & LEFT_PAIR ) >> 2 | (c & RIGHT_PAIR ) << 2);
    c = ((c & LEFT_ONES ) >> 1 | (c & RIGHT_ONES ) << 1);
    return (c);
}

int Is2ndAnd6thOn(unsigned char c)
{
    assert(NULL != c);
    
    return ((c & MASK_6AND2) == MASK_6AND2); 
}

int Is2ndOr6thOn(unsigned char c)
{
    assert(NULL != c);
    
    return (0 != (c & MASK_6AND2));
}

unsigned char Swap3rdAnd5th(unsigned char c)
{
    size_t bit_swap_1 = 3;
    size_t bit_swap_2 = 5;
    unsigned char mask = 0;
    unsigned char bit_1 = 0;
    unsigned char bit_2 = 0;

    assert(NULL != c);
    
    bit_1 = (c >> bit_swap_1) & 1;              
    bit_2 = (c >> bit_swap_2) & 1;
    
    mask = bit_1 ^ bit_2;
    mask = (mask << bit_swap_1) | (mask << bit_swap_2);

    c ^= mask;

    return (c);
}

unsigned int ClosestDivisibleBy16(unsigned int n)
{
	return (n & (unsigned int)DIV_BY_16);
}

void SwapWithoutTemp(int *a, int *b)
{
	assert(NULL != a);
	assert(NULL != b);

  	*a = *a ^ *b;
  	*b = *b ^ *a;
  	*a = *a ^ *b;
}

size_t SetBitsCountV1(int num)
{
    return (CountBits(num)); 
}

size_t SetBitsCountV2(int num)
{
    int bin_handler_1 = 0;
    int bin_handler_2 = 0;
    
    assert(0 != num);

    if(4 != sizeof(num))
    {
        return (9999);
    }

    bin_handler_1 = (num >> 0) & MASK_ONES;
    bin_handler_2 = (num >> 1 ) & MASK_ONES;
    num = bin_handler_1 + bin_handler_2;

    bin_handler_1 = (num >> 0) & MASK_PAIR;
    bin_handler_2 = (num >> 2) & MASK_PAIR;
    num = bin_handler_1 + bin_handler_2;
    
    bin_handler_1 = (num >> 0) & MASK_NIBL;
    bin_handler_2 = (num >> 4) & MASK_NIBL;
    num = bin_handler_1 + bin_handler_2;                       

    bin_handler_1 = (num >> 0) & MASK_BYTE;
    bin_handler_2 = (num >> 8) & MASK_BYTE;
    num = bin_handler_1 + bin_handler_2;

    bin_handler_1 = (num >> 0) & MASK_HALF;
    bin_handler_2 = (num >> 16) & MASK_HALF;
    num = bin_handler_1 + bin_handler_2;

    return (num);
}

void FloatAnalysis(float user_input)
{
	float *input_1 = &user_input;
    int *ptr_input = (int*)input_1;
    int x = 31;
	
	printf("\n");
    for(; x >= 0; --x)
    { 
        if((*ptr_input & (1 << x)) == 0)
        {
            printf("0");
        }
        else
        {
            printf("1");
        }
    }
    printf("\n");
}
