/*

Created by Sam
Reviwed by Sergey

*/

#include <stdio.h>	/* size_t() */
#include <assert.h> /* assert() */
#include <limits.h>		/* CHAR_BIT */

#include "bitarray.h"

#define SET_64_BIT (0xFFFFFFFFFFFFFFFF)
#define RESET_64_BIT (0x0)

#define BYTES_IN_BITARRAY (sizeof(bitsarr_t))
#define BITS_IN_BITARRAY (BYTES_IN_BITARRAY * CHAR_BIT)
#define MASK_IDX_BIT_ON(idx) ((bitsarr_t)0x1 << (idx))

#define MASK_FIRST_BYTE (0xFF)

#define LEFT_BYTE (0xFF00FF00FF00FF00)
#define RIGHT_BYTE (0x00FF00FF00FF00FF)

#define LEFT_BYTES (0xFFFF0000FFFF0000)
#define RIGHT_BYTES (0x0000FFFF0000FFFF)

#define LEFT_NIBL (0xF0F0F0F0F0F0F0F0)
#define RIGHT_NIBL (0x0F0F0F0F0F0F0F0F)

#define LEFT_PAIR (0xCCCCCCCCCCCCCCCC)
#define RIGHT_PAIR (0x3333333333333333)

#define LEFT_ONES (0xAAAAAAAAAAAAAAAA)
#define RIGHT_ONES (0x5555555555555555)

#define MASK_NIBL (0x0F)
#define MASK_PAIR (0x33)
#define MASK_ONES (0x55)

#define NULL_TERMINATOR_SYMBOL ('\0')

static unsigned char mirror_lut[256] = {0};
static unsigned char count_lut[256] = {0};
static int is_count_lut_filled = 0;
static int is_mirror_lut_filled = 0;
static void FillCountLut();
static void FillMirrorLut();

#define MIR_LUT_N_ELEMENTS (sizeof(mirror_lut) / sizeof(mirror_lut[0]))
#define COUNT_LUT_N_ELEMENTS (sizeof(count_lut) / sizeof(count_lut[0]))

bitsarr_t BitArraySetAll(bitsarr_t bit_array)
{
	return (bitsarr_t)SET_64_BIT;
	(void)bit_array; 
}

bitsarr_t BitArrayResetAll(bitsarr_t bit_array)
{
	return (bitsarr_t)RESET_64_BIT;
	(void)bit_array; 
}

bitsarr_t BitArraySetOn(bitsarr_t bit_array, size_t idx)
{
	assert(BITS_IN_BITARRAY > idx);
	return (bit_array | MASK_IDX_BIT_ON(idx));
}

bitsarr_t BitArraySetOff(bitsarr_t bit_array, size_t idx)
{
	assert(BITS_IN_BITARRAY > idx);
	return (bit_array & ~MASK_IDX_BIT_ON(idx));
}

int BitArrayGetVal(bitsarr_t bit_array, size_t idx)
{
	assert(BITS_IN_BITARRAY > idx);
	return ((bit_array >> idx) & MASK_IDX_BIT_ON(0));
}

bitsarr_t BitArraySetBit(bitsarr_t bit_array, size_t idx, int value)
{
	assert(BITS_IN_BITARRAY > idx);
	assert(1 == value && 0 == value);
	
	return (BitArraySetOff(bit_array, idx) | ((size_t)value << idx));
}

bitsarr_t BitArrayFlip(bitsarr_t bit_array, size_t idx)
{
	bitsarr_t mask = 0;
	
	assert(BITS_IN_BITARRAY > idx);
	
	mask = MASK_IDX_BIT_ON(idx);
	return (bit_array ^= mask);
}

bitsarr_t BitArrayMirror(bitsarr_t bit_array)
{
	bit_array = ((bit_array & LEFT_ONES ) >> 1 | (bit_array & RIGHT_ONES ) << 1);
	bit_array = ((bit_array & LEFT_PAIR ) >> 2 | (bit_array & RIGHT_PAIR ) << 2);
	bit_array = ((bit_array & LEFT_NIBL ) >> 4 | (bit_array & RIGHT_NIBL) << 4);
	bit_array = ((bit_array & LEFT_BYTE ) >> 8 | (bit_array & RIGHT_BYTE) << 8);
	bit_array = ((bit_array & LEFT_BYTES ) >> 16 | (bit_array & RIGHT_BYTES) << 16);
	
	bit_array = ((bit_array >> 32) | (bit_array << 32));
    
    return (bit_array);
}

bitsarr_t BitArrayRotateRight(bitsarr_t bit_array, size_t steps)
{
	bit_array = (bit_array >> steps) | (bit_array << (BITS_IN_BITARRAY - steps));
	return (bit_array);
}

bitsarr_t BitArrayRotateLeft(bitsarr_t bit_array, size_t steps)
{
	bit_array = (bit_array << steps) | (bit_array >> (BITS_IN_BITARRAY - steps));
	return (bit_array);
}

size_t BitArrayCountOn(bitsarr_t bit_array)
{
	size_t count = 0;

    while (0 != bit_array) 
    {
        count += bit_array & MASK_IDX_BIT_ON(0);
        bit_array >>= 1;
    }
    return count;
}

size_t BitArrayCountOff(bitsarr_t bit_array)
{
    return (BITS_IN_BITARRAY - BitArrayCountOn(bit_array));
}

char *BitArrayToString(bitsarr_t bit_array, char *string)
{
	int bit_n = 0;

	assert(NULL != string);
	
	for (bit_n = BITS_IN_BITARRAY - 1; 0 <= bit_n; --bit_n)
	{
		*string = BitArrayGetVal(bit_array, bit_n) + '0';	
		++string;
	}
	
	*string = NULL_TERMINATOR_SYMBOL;

	return string;
}

size_t BitArrayCountOnLUT(bitsarr_t bit_array)
{
	size_t count = 0;
	
	if(!is_count_lut_filled)
	{
		FillCountLut();	
	}
	
	while (0 != bit_array) 
    {
        count += count_lut[bit_array & MASK_FIRST_BYTE];
        bit_array >>= CHAR_BIT;
    }
    return count;
}



bitsarr_t BitArrayMirrorLUT(bitsarr_t bit_array)
{
	bitsarr_t res = 0;
	unsigned char *char_ptr_input = (unsigned char *)&bit_array;
	unsigned char *char_ptr_result = (unsigned char *)&res + sizeof(res) - 1;
	size_t byte_step = 0;
	
	if(!is_mirror_lut_filled)
	{
		FillMirrorLut();	
	}

	
	for(; BYTES_IN_BITARRAY > byte_step; ++byte_step)
	{
		*char_ptr_result = mirror_lut[*char_ptr_input];
		++char_ptr_input;
		--char_ptr_result;
	}

	return res;
}

static void FillMirrorLut()
{
	size_t index = 0;

	for(; MIR_LUT_N_ELEMENTS > index; ++index)
	{
		unsigned char value = index;

		value = ((value >>  4) & MASK_NIBL) | (value & MASK_NIBL) <<  4;
		value = ((value >>  2) & MASK_PAIR) | (value & MASK_PAIR) <<  2;
		value = ((value >>  1) & MASK_ONES) | (value & MASK_ONES) <<  1;	

		mirror_lut[index] = value;
	}

	is_mirror_lut_filled = 1;
}

static void FillCountLut()
{
	size_t index = 0;

	for(; index < COUNT_LUT_N_ELEMENTS; ++index)
	{
		count_lut[index] = BitArrayCountOn((bitsarr_t)index);
	}

	is_count_lut_filled = 1;
}



