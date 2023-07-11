/*
Reviewed by Berhanu
Contains definitions of ItoaBase10(), AtoiBase10(), ItoaBaseUp36(),
AtoiBaseUp36(), PrintCharsIn1And2Not3() and IsLittleEndian()
functions. 
Created by Sam 
*/

#include <stdio.h> 		/* printf() */
#include <ctype.h>		/* ctype(), toupper() */
#include <assert.h> 	/* assert() */
#include "ws11.h"

#define NULL_TERMINATOR_SYMBOL ('\0')
#define ASCII_ZERO_SYMBOL (48)
#define ASCII_TABLE_SIZE (256)
#define ASCII_A_SYMBOL (65)
#define ASCII_SPACE_SYMBOL (32)
#define ASCII_DASH_SYMBOL (45)
#define MASK_BIN_ONE (0X1)
#define LAST_DIGIT (10)
#define IS_SYMBOL_FITS_BASE ((*src - 'A' + 10) < (long) base)
#define IS_LITTLE_ENDIAN (1 == *(char *)"\1")

static void ReverseString(char *string_begins, char *string_ends);
static char ConvertToChar(int num);
static int ConvertToInt(char c);
static void Swap(char *a, char *b);
int RunIsLittleEndianMacro();


static void Swap(char *a, char *b)
{
    char tmp = 0;
    
    assert(NULL != *a);
    assert(NULL != *b);
    
    tmp = (*a);
    *a = (*b);
    *b = tmp;
}

static void ReverseString(char *string_begins, char *string_ends)
{

    assert(NULL != string_begins);
    assert(NULL != string_ends);

    while(string_begins < string_ends)
    {
		Swap(string_begins, string_ends);
        ++string_begins;
        --string_ends;
    }
}

static char ConvertToChar(int num)
{
    if (0 <= num && 9 >= num)
    {
       return (char)(num + '0');
    }
    return (char)(num - 10 + ASCII_A_SYMBOL);
}

static int ConvertToInt(char c)
{
    if (c >= '0' && c <= '9')
    {
        return (int)c - '0';
    }
    return (int)c - ASCII_A_SYMBOL + 10;
}

void ItoaBase10(int num, char *dest)
{
	char *runner = NULL;
	char *start_ch = NULL;
	int last_digit = 0;
	
	assert(NULL != dest);
	
	start_ch = dest;
	
	if(0 > num)
	{
		num = -num;
		*start_ch = ASCII_DASH_SYMBOL;
		++start_ch;
	}
	
	runner = start_ch;
	
	do
	{
		last_digit = num % LAST_DIGIT;
		*runner = ASCII_ZERO_SYMBOL + last_digit;
		num /= LAST_DIGIT;
		++runner;
	}while(0 < num);
	
	*runner = NULL_TERMINATOR_SYMBOL;
	ReverseString(start_ch, runner - 1);
}

int AtoiBase10(const char *src)
{
	int result = 0;
	int sign = 1;
	
	assert(NULL != src);
	
	while(ASCII_SPACE_SYMBOL == *src)
	{
		++src;
	}
	
	if(ASCII_DASH_SYMBOL == *src)
	{
		sign = -sign;
		++src;
	}
	
	while(NULL_TERMINATOR_SYMBOL != *src && 0 == isalpha(*src))
	{
		result *= LAST_DIGIT;
		result += *src - ASCII_ZERO_SYMBOL;
		++src;
	}
	
	return (result * sign);
}

void ItoaBaseUp36(int num, size_t base, char *dest)
{
	char *runner = NULL;
	char *start_ch = NULL;
	int last_digit = 0;
	
	assert(NULL != dest);
	
	start_ch = dest;
	
	if(0 > num)
	{
		num = -num;
		*start_ch = ASCII_DASH_SYMBOL;
		++start_ch;
	}
	
	runner = start_ch;
	
	do
	{
		last_digit = num % base;
		*runner = ConvertToChar(last_digit);
		num = num / base;
		++runner;
	}while(0 < num);
	
	*runner = NULL_TERMINATOR_SYMBOL;
	
	ReverseString(start_ch, runner - 1);
}

int AtoiBaseUp36(const char *src, size_t base)
{
	int result = 0;
	int sign = 1;
	int num = 0;
	
	char upper_case_symbol = ASCII_ZERO_SYMBOL;
	
	assert(NULL != src);
	
	while(ASCII_SPACE_SYMBOL == *src)
	{
		++src;
	}
	
	if(ASCII_DASH_SYMBOL == *src)
	{
		sign = -sign;
		++src;
	}
	
	while(NULL_TERMINATOR_SYMBOL != *src && IS_SYMBOL_FITS_BASE)
	{
		upper_case_symbol = toupper(*src);
		num = ConvertToInt(upper_case_symbol);
		result = result * base + num;
		++src;
	}
	
	return (result * sign);
}

void PrintCharsIn1And2Not3(char chars1[], size_t size1, char chars2[], 
    size_t size2, char chars3[], size_t size3)
{
	int char_lut[ASCII_TABLE_SIZE] = {0};
	unsigned char cur_element = ASCII_ZERO_SYMBOL;
    size_t i = 0;
    int is_alphabetic = 0;

    assert(NULL != chars1);
    assert(NULL != chars2);
    assert(NULL != chars3);
    
    for(i = 0; i < size3; ++i)
    {
    	cur_element = (unsigned char)chars3[i];
    	char_lut[cur_element] = -1;
    }
    
    for(i = 0; i < size2; ++i)
    {
    	cur_element = (unsigned char)chars2[i];
    	
    	if(-1 != char_lut[cur_element])
    	{
    		char_lut[cur_element] = 1;
    	}
    }
    
    for(i = 0; i < size1; ++i)
    {
    	cur_element = (unsigned char)chars1[i];
    	is_alphabetic = isalpha(chars1[i]);
    	
    	if(1 == char_lut[cur_element] && 0 != is_alphabetic)
    	{
    		char_lut[cur_element] = 0;
    		printf("%c", chars1[i]);
    	}
    }
    printf("\n");
}

int IsLittleEndian()
{
   unsigned int first_bit_set = MASK_BIN_ONE;
   char *first_byte = (char*)&first_bit_set;
   if (0 != *first_byte)
   {   
       return (1);
   }
   return (0);
}


int RunIsLittleEndianMacro()
{
    return (IS_LITTLE_ENDIAN);
}
