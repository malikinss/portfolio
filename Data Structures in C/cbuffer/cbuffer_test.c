/*
*****************************
* Title : cbuffer test file	*
* Author: Sam				*
* Reviewer: Vladimir		*
* Date : 18.04.2023			*
*****************************
*/
#include <stdio.h> /* printf() */
#include <string.h> /* strlen() */

#include "cbuffer.h"

static void CheckBufSiz(cbuffer_t *cbuffer1, cbuffer_t *cbuffer2, 
										size_t result1, size_t result2);
static void CheckIsEmpty(cbuffer_t *cbuffer1, cbuffer_t *cbuffer2, 
										int result1, int result2);
static void CheckFreeSpace(cbuffer_t *cbuffer1, cbuffer_t *cbuffer2, 
										size_t result1, size_t result2);
static void CheckWrite(cbuffer_t *cbuffer1, cbuffer_t *cbuffer2, char *word1,
	char *word2, size_t write1, size_t write2, size_t result1, size_t result2);
static void CheckFirstRead(cbuffer_t *cbuffer1, cbuffer_t *cbuffer2, char *buffer,
					size_t read1, size_t read2, size_t result1, size_t result2);
static void CheckSecondRead(cbuffer_t *cbuffer1, cbuffer_t *cbuffer2, char *buffer,
					size_t read1, size_t read2, size_t result1, size_t result2);

int main()
{
	size_t size1 = 15;
	size_t size2 = 3;
	cbuffer_t *cbuffer1 = CBufferCreate(size1);
	cbuffer_t *cbuffer2 = CBufferCreate(size2);
	char word1[] = "HELLO";
	char word2[] = "hi";
	char word3[] = "0123456789ABCDEF";
	char word4[] = "hihihi";
	char buffer[50] = {0}; 

	printf("\n\t\t~~~CREATING cbuffer1 and cbuffer2~~~\n");
	CheckBufSiz(cbuffer1, cbuffer2, size1, size2);
	CheckFreeSpace(cbuffer1, cbuffer2, size1, size2);
	CheckIsEmpty(cbuffer1, cbuffer2, 1, 1);

	printf("\n\t\t~~~WRITING SIMPLE EXAMPLE~~~\n");
	CheckWrite(cbuffer1, cbuffer2, word1, word2, 
			strlen(word1), strlen(word2), strlen(word1), strlen(word2));
	CheckBufSiz(cbuffer1, cbuffer2, size1, size2);
	CheckFreeSpace(cbuffer1, cbuffer2, size1 - 5, size2 - 2);
	CheckIsEmpty(cbuffer1, cbuffer2, 0, 0);

	printf("\n\t\t~~~READING SIMPLE EXAMPLE~~~\n");
	CheckFirstRead(cbuffer1, cbuffer2, buffer,
		strlen(word1), strlen(word2), strlen(word1), strlen(word2));
	CheckBufSiz(cbuffer1, cbuffer2, size1, size2);
	CheckFreeSpace(cbuffer1, cbuffer2, size1, size2);
	CheckIsEmpty(cbuffer1, cbuffer2, 1, 1);

	printf("\n\t\t~~~OVERWRITING~~~\n");
	CheckWrite(cbuffer1, cbuffer2, word3, word4, 
						strlen(word3), strlen(word4), size1, size2);
	CheckBufSiz(cbuffer1, cbuffer2, size1, size2);
	CheckFreeSpace(cbuffer1, cbuffer2, 0, 0);
	CheckIsEmpty(cbuffer1, cbuffer2, 0, 0);

	printf("\n\t\t~~~READING HELF SECOND EXAMPLE~~~\n");
	CheckSecondRead(cbuffer1, cbuffer2, buffer, strlen(word3) / 2,
			strlen(word4) / 2, strlen(word3) / 2, strlen(word4) / 2);
	CheckBufSiz(cbuffer1, cbuffer2, size1, size2);
	CheckFreeSpace(cbuffer1, cbuffer2, strlen(word3) / 2, strlen(word4) / 2);
	CheckIsEmpty(cbuffer1, cbuffer2, 0, 1);

	printf("\n\t\t~~~DESTROYING~~~\n\t\t    LOOK HERE |          |\n");
	printf("\t\t\t      v          v\n");
	CBufferDestroy(cbuffer1);
	CBufferDestroy(cbuffer2);

	return 0;
}


static void CheckBufSiz(cbuffer_t *cbuffer1, cbuffer_t *cbuffer2, 
										size_t result1, size_t result2)
{
	printf("\nCBufferBufSiz(cbuffer1)\t\t\t%ld == |%ld|\n",
										result1, CBufferBufSiz(cbuffer1));
	printf("CBufferBufSiz(cbuffer2)\t\t\t%ld == |%ld|\n",
										result2, CBufferBufSiz(cbuffer2));	
}

static void CheckIsEmpty(cbuffer_t *cbuffer1, cbuffer_t *cbuffer2, 
										int result1, int result2)
{
	printf("\nCBufferIsEmpty(cbuffer1)\t\t%d == |%d|\n", 
								result1, CBufferIsEmpty(cbuffer1));
	printf("CBufferIsEmpty(cbuffer2)\t\t%d == |%d|\n", 
								result2, CBufferIsEmpty(cbuffer2));
}

static void CheckFreeSpace(cbuffer_t *cbuffer1, cbuffer_t *cbuffer2, 
										size_t result1, size_t result2)
{
	printf("\nCBufferFreeSpace(cbuffer1)\t\t%ld == |%ld|\n",
									result1, CBufferFreeSpace(cbuffer1));
	printf("CBufferFreeSpace(cbuffer2)\t\t%ld == |%ld|\n", 
									result2, CBufferFreeSpace(cbuffer2));	
}

static void CheckWrite(cbuffer_t *cbuffer1, cbuffer_t *cbuffer2, char *word1,
	char *word2, size_t write1, size_t write2, size_t result1, size_t result2)
{
	printf("\nWrite to cbuffer1\t\t\t%ld == |%ld|\n", 
						result1, CBufferWrite(cbuffer1, word1, write1));
	printf("Write to cbuffer2\t\t\t%ld == |%ld|\n", 
						result2, CBufferWrite(cbuffer2, word2, write2));

}

static void CheckFirstRead(cbuffer_t *cbuffer1, cbuffer_t *cbuffer2, char *buffer,
					size_t read1, size_t read2, size_t result1, size_t result2)
{
	printf("Read 'HELLO' from cbuffer1\t\t%ld == |%ld|\n",
							result1, CBufferRead(cbuffer1, buffer, read1));
	printf("Buffer\t\t\t\t\tHELLO == |%s|\n", buffer);

	printf("Read 'hi' from cbuffer2\t\t\t%ld == |%ld|\n",
							result2, CBufferRead(cbuffer2, buffer, read2));
	printf("Buffer\t\t\t\t\thiLLO == |%s|\n", buffer);	
}

static void CheckSecondRead(cbuffer_t *cbuffer1, cbuffer_t *cbuffer2, char *buffer,
					size_t read1, size_t read2, size_t result1, size_t result2)
{
	printf("Read '01234567' from cbuffer1\t\t%ld == |%ld|\n",
							result1, CBufferRead(cbuffer1, buffer, read1));
	printf("Buffer\t\t\t\t\t01234567 == |%s|\n", buffer);

	printf("Read 'hih' from cbuffer2\t\t%ld == |%ld|\n",
							result2, CBufferRead(cbuffer2, buffer, read2));
	printf("Buffer\t\t\t\t\thih34567 == |%s|\n", buffer);	
}

