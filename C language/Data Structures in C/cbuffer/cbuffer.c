/*
*****************************************
* Title : cbuffer function definitions	*
* Author: Sam							*
* Reviewer: Vladimir					*
* Date : 18.04.2023						*
*****************************************
*/

#include <stdlib.h> /* malloc, free */
#include <assert.h> /* assert */
#include <string.h> /* memcpy */

#include "cbuffer.h"

struct cbuffer
{
    size_t capacity;
    size_t size;
    size_t read;
    char buffer[1];
};

static void ReadData(size_t read, char *buffer, \
size_t capacity, size_t bytes_to_read, void *dest);
static void WriteData(size_t write, char *buffer, \ 
size_t capacity, size_t bytes_to_write, const void *src);

cbuffer_t *CBufferCreate(size_t capacity)
{
    size_t cbufsize = sizeof(struct cbuffer);
    size_t buffsize = (sizeof(char) * capacity - sizeof(size_t));
    cbuffer_t *new_cbuffer = (cbuffer_t *)malloc(cbufsize + buffsize);

    if (NULL == new_cbuffer)
    {
        return (NULL);
    }

    new_cbuffer->size = 0;
    new_cbuffer->read = 0;
    new_cbuffer->capacity = capacity;

    return (new_cbuffer);
}

void CBufferDestroy(cbuffer_t *cbuffer)
{
    assert(NULL != cbuffer);

    free(cbuffer);
    cbuffer = NULL;
}

size_t CBufferFreeSpace(const cbuffer_t *cbuffer)
{
    assert(NULL != cbuffer);

    return ((cbuffer->capacity) - (cbuffer->size));
}

size_t CBufferBufSiz(const cbuffer_t *cbuffer)
{
    assert(NULL != cbuffer);

    return (cbuffer->capacity);
}

int CBufferIsEmpty(const cbuffer_t *cbuffer)
{
    assert(NULL != cbuffer);

    return (!cbuffer->size);
}

size_t CBufferWrite(cbuffer_t *cbuffer, const void *src, size_t count)
{
    size_t capacity = 0;
    size_t read = 0;
    char *buffer = NULL;
    size_t available_space = 0;
    size_t bytes_to_write = 0;
    size_t write_place = 0;

    assert(NULL != cbuffer);
    assert(NULL != src);

    capacity = cbuffer->capacity;
    read = cbuffer->read;
    buffer = cbuffer->buffer;

    available_space = CBufferFreeSpace(cbuffer);
    bytes_to_write = count < available_space ? count : available_space;
    write_place = (read + cbuffer->size) % capacity;

    WriteData(write_place, buffer, capacity, bytes_to_write, src);

    cbuffer->size += bytes_to_write;

    return (bytes_to_write);
}

size_t CBufferRead(cbuffer_t *cbuffer, void *dest, size_t count)
{
    size_t capacity = 0;
    size_t read = 0;
    char *buffer = NULL;
    size_t bytes_to_read = 0;

    assert(NULL != cbuffer);
    assert(NULL != dest);

    read = cbuffer->read;
    buffer = cbuffer->buffer;
    capacity = cbuffer->capacity;

    bytes_to_read = count > cbuffer->size ? cbuffer->size : count;

    ReadData(read, buffer, capacity, bytes_to_read, dest);

    cbuffer->size -= bytes_to_read;
    cbuffer->read = (read + bytes_to_read) % capacity;

    return (bytes_to_read);
}

static void ReadData(size_t read, char *buffer, size_t capacity, size_t bytes_to_read, void *dest)
{
    size_t bytes_to_end = capacity - read;
    size_t bytes_remain = 0;

    if (bytes_to_end >= bytes_to_read)
    {
        memcpy(dest, buffer + read, bytes_to_read);
    }
    else
    {
        memcpy(dest, buffer + read, bytes_to_end);
        bytes_remain = bytes_to_read - bytes_to_end;
        memcpy((char *)dest + bytes_to_end, buffer, bytes_remain);
    }
}

static void WriteData(size_t write, char *buffer, size_t capacity, size_t bytes_to_write, const void *src)
{
    size_t bytes_to_end = capacity - write;
    size_t bytes_remain = 0;

    if (bytes_to_end >= bytes_to_write)
    {
        memcpy(buffer + write, src, bytes_to_write);
    }
    else
    {
        memcpy(buffer + write, src, bytes_to_end);
        bytes_remain = bytes_to_write - bytes_to_end;
        memcpy(buffer, (char *)src + bytes_to_end, bytes_remain);
    }
}
