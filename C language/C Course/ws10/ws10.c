/*	
	Reviewed by Sergey
	Contains definitions of different implementation library
	memset(), memcpy() and memmove() functions. 
	Created by Sam 
*/

#include <assert.h>	/* assert() */	
#include "ws10.h"

static void PutByByte(int c, const size_t count, unsigned char **runner_p);
static void PutByChunk(const unsigned char *chunk_buff, 
						const size_t count, unsigned char **runner_p);
						
static void CopyByByte(const size_t count, unsigned char **runner_dest_ptr, 
					const unsigned char **runner_src_ptr);
static void CopyByChunk(const size_t count, unsigned char **runner_dest_ptr, 
							const unsigned char **runner_src_ptr);

						
static size_t FindBytesBeforeAlign(const void *s, const size_t n);
static void FillChunkBuff(int c, unsigned char *chunk_buff);
static void SplitToChunksAndBytes(size_t *bytes_after_align,
								  size_t *n_chunks_to_fill, const size_t n);


void *Memset(void *s, int c, size_t n)
{
	size_t bytes_before_align = 0;
	size_t bytes_after_align = 0;
	size_t n_chunks_to_fill = 0;
	unsigned char *runner = NULL;
	unsigned char chunk_buff[MY_WORD_SIZE] = {0};

	assert(NULL != s);

	runner = (unsigned char *)s;

	bytes_before_align = FindBytesBeforeAlign(s, n);
	PutByByte(c, bytes_before_align, &runner);

	n -= bytes_before_align;

	SplitToChunksAndBytes(&bytes_after_align, &n_chunks_to_fill, n);

	FillChunkBuff(c, chunk_buff);
	PutByChunk(chunk_buff, n_chunks_to_fill, &runner);
	PutByByte(c, bytes_after_align, &runner);

	return (s);
}

void *Memcpy(void *dest, const void *src, size_t n)
{
	size_t bytes_before_align = 0;
	size_t bytes_after_align = 0;
	size_t n_chunks_to_fill = 0;
	unsigned char *runner_dest = NULL;
	const unsigned char *runner_src = NULL;

	assert(NULL != src);
	assert(NULL != dest);

	runner_dest = (unsigned char *)dest;	
	runner_src = (unsigned char *)src;

	bytes_before_align = FindBytesBeforeAlign(dest, n);
	if(bytes_before_align != FindBytesBeforeAlign(src, n))
	{
		CopyByByte(n, &runner_dest, &runner_src);
	}
	else
	{	
		CopyByByte(bytes_before_align, &runner_dest, &runner_src);
		n -= bytes_before_align;
		SplitToChunksAndBytes(&bytes_after_align, &n_chunks_to_fill, n);
		CopyByChunk(n_chunks_to_fill, &runner_dest, &runner_src);
		CopyByByte(bytes_before_align, &runner_dest, &runner_src);
	}

	return (dest);
}

void *Memmove(void *dest, const void *src, size_t n)
{
	unsigned char *runner_dest = NULL;
	const unsigned char *runner_src = NULL;	

	assert(NULL != src);
	assert(NULL != dest);
	
	runner_dest = dest;
	runner_src = src;

	if(src < dest)
	{
		runner_dest += (n - 1);
		runner_src += (n - 1);

		while(0 != n)
		{
			*runner_dest = *runner_src;
			--runner_dest;
			--runner_src;
			--n;
		}
	}
	else
	{
		Memcpy(dest, src, n);
	}

	return dest;
}

static void SplitToChunksAndBytes(size_t *bytes_after_align, 
								  size_t *n_chunks_to_fill, const size_t n)
{
	assert(NULL != bytes_after_align);
	assert(NULL != n_chunks_to_fill);

	*bytes_after_align = n % MY_WORD_SIZE;
	*n_chunks_to_fill = n / MY_WORD_SIZE;
}

static size_t FindBytesBeforeAlign(const void *s, const size_t n)
{
	size_t reminder = 0;
	size_t bytes_before_align = 0;

	assert(NULL != s);

	reminder = ((unsigned long)s & (MY_WORD_SIZE - 1));

	if(0 != reminder)
	{
		bytes_before_align = MY_WORD_SIZE - reminder;
	}
	else
	{
		bytes_before_align = reminder;
	}

	if(bytes_before_align > n)
	{
		bytes_before_align = n;
	}

	return bytes_before_align;
}

static void FillChunkBuff(int c, unsigned char *chunk_buff)
{
	size_t i = 0;
	unsigned char char_c = (unsigned char) c;

	assert(NULL != chunk_buff);
	
	for(i = 0; i < MY_WORD_SIZE; ++i)
	{
		chunk_buff[i] = char_c;
	}

}

static void PutByByte(int c, const size_t count, unsigned char **runner_p)
{
	unsigned char char_c = (unsigned char) c;
	size_t i = 0;

	assert(NULL != runner_p);
	assert(NULL != *runner_p);

	for(i = 0; i < count; ++i)
	{
		**runner_p = char_c;
		*runner_p += 1;
	}
}

static void PutByChunk(const unsigned char *chunk_buff, 
						const size_t count, unsigned char **runner_p)
{
	size_t i = 0;

	assert(NULL != runner_p);
	assert(NULL != *runner_p);
	assert(NULL != chunk_buff);

	for(i = 0; i < count; ++i)
	{
		size_t *temp_ptr = (size_t *)(*runner_p);

		*temp_ptr = *(size_t *)chunk_buff;
		*runner_p += MY_WORD_SIZE;
	}
}

static void CopyByByte(const size_t count, unsigned char **runner_dest_ptr, 
					const unsigned char **runner_src_ptr)
{
	size_t i = 0;

	assert(NULL != runner_dest_ptr);
	assert(NULL != *runner_dest_ptr);
	assert(NULL != runner_src_ptr);
	assert(NULL != *runner_src_ptr);

	for(; i < count; ++i)
	{
		**runner_dest_ptr = **runner_src_ptr;
		*runner_dest_ptr += 1;
		*runner_src_ptr += 1;
	}
}


static void CopyByChunk(const size_t count, unsigned char **runner_dest_ptr, 
							const unsigned char **runner_src_ptr)
{
	size_t i = 0;

	assert(NULL != runner_dest_ptr);
	assert(NULL != *runner_dest_ptr);
	assert(NULL != runner_src_ptr);
	assert(NULL != *runner_src_ptr);

	for(i = 0; i < count; ++i)
	{
		size_t *temp_ptr = (size_t *)(*runner_dest_ptr);

		*temp_ptr = *(size_t *)(*runner_src_ptr);
		*runner_dest_ptr += MY_WORD_SIZE;
		*runner_src_ptr += MY_WORD_SIZE;
	}
}

