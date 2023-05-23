/*
*********************************************************	
* Title : Header file, contains declarations:			* 
*				type cbuffer_t,							*
*				CBufferCreate(),						*			
*				CBufferDestroy(), 						*	
*				CBufferFreeSpace(), 					*
*				CBufferBufSiz(), 						*
*				CBufferIsEmpty(),						*
*				CBufferWrite(), 						*
*				CBufferRead().							*
*														*
*		Function definitions in the cbuffer.c file. 	*
* Author: Sam Malikin									*
* Reviewer: Vladimir									*
* Date : 18.04.2023										*
*********************************************************	
*/

#ifndef __CBUFFER_H_ILRD__
#define __CBUFFER_H_ILRD__

#include <stddef.h> /* size_t */

typedef struct cbuffer cbuffer_t;

/*
DESCRIPTION
	Create a new circular buffer. Memory will be allocated.
	In case of allocation failure, returns NULL.
	User is responsible for destroying circular buffers.
RETURN
	Pointer to the created circular buffer.
	Or NULL if allocation failed.
INPUT
	capacity: number of bytes to allocate the circular buffer.
*/
cbuffer_t *CBufferCreate(size_t capacity);

/*
DESCRIPTION
	Destroyes the circular buffer by freeing all the allocated memory.
	All remaining data will be lost.
	The user is responsible for handling dangling pointers.
RETURN
	There is no return for this function.
INPUT
	cbuffer: a pointer to a circular buffer.
*/
void CBufferDestroy(cbuffer_t *cbuffer);

/*
DESCRIPTION
	Returns how many bytes are still availible for writing
	in a circular buffer.
RETURN
	Number of free bytes in a circular buffer.
INPUT
	cbuffer: a pointer to a circular buffer.
*/
size_t CBufferFreeSpace(const cbuffer_t *cbuffer);

/*
DESCRIPTION
	Returns the capacity of a circular buffer.
RETURN
	Capacity of a circular buffer in bytes.
INPUT
	cbuffer: a pointer to a circular buffer.
*/
size_t CBufferBufSiz(const cbuffer_t *cbuffer);

/*
DESCRIPTION
	Checks wherther the circular buffer is empty.
RETURN
	1 - if the circular buffer is empty.
	0 - if the circular buffer is not empty.	
INPUT
	cbuffer: a pointer to a circular buffer.
*/
int CBufferIsEmpty(const cbuffer_t *cbuffer);

/*
DESCRIPTION
	Function writes bytes from src to the circular buffer.
RETURN
	Number of written bytes.
INPUT
	cbuffer: a pointer to a circular buffer.
	scr: pointer to data that should be written to the buffer.
	count: number of bytes that should be written.
*/
size_t CBufferWrite(cbuffer_t *cbuffer, const void *src, size_t count);

/*
DESCRIPTION
	Function reads bytes from the circular buffer to user's dest.
RETURN
	Number of read bytes.
INPUT
	cbuffer: a pointer to a circular buffer.
	dest: pointer to data that should be read from the buffer.
	count: number of bytes that should be read.
*/
size_t CBufferRead(cbuffer_t *cbuffer, void *dest, size_t count);

#endif /* __CBUFFER_H_ILRD__ */

