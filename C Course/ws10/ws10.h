/* 
	Reviewed by Sergey
	Header file, contains description of different implementation
	library memset(), memcpy() and memmove() functions. Function
	definitions in the ws_10.c file. 
	Created by Sam
*/

#ifndef __WS10_H__
#define __WS10_H__

#include <stddef.h>	/* size_t */

#define MY_WORD_SIZE (sizeof(size_t))


/*DESCRIPTION:
	Function copies the character "int c" (an unsigned char) 
	to the first "n" characters of the string pointed to, by
	the argument "s".

RETURN: 
	This function returns a pointer to the memory area str.

PARAMS:
s − This is a pointer to the block of memory to fill.

c − This is the value to be set. The value is passed as an 
	int, but the function fills the block of memory using 
	the unsigned char conversion of this value.

n − This is the number of bytes to be set to the value.
*/
void *Memset(void *s, int c, size_t n);

/*DESCRIPTION: 
	Function copies n characters from memory area src to memory
	area dest.

RETURN: 
	This function returns a pointer to dest.

PARAMS:
dest −  This is pointer to the destination array where the content
 	is to be copied, type-casted to a pointer of type void*.

src − This is pointer to the source of data to be copied,
 	type-casted to a pointer of type void*.

n − This is the number of bytes to be copied.
*/
void *Memcpy(void *dest, const void *src, size_t n);

/*DESCRIPTION: 
	Function copies n characters from src to dest, but for
	overlapping memory blocks, Memmove() is a safer approach
	than Memcpy().

RETURN: 
	This function returns a pointer to the dest.

PARAMS:
dest − This is a pointer to the destination array where the 
	content is to be copied, type-casted to a pointer of type void*.

src  − This is a pointer to the source of data to be copied,
	type-casted to a pointer of type void*.

n − This is the number of bytes to be copied.
*/
void *Memmove(void *dest, const void *src, size_t n);

#endif /* __WS10_H__ */

