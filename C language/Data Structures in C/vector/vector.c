/*

This file contains implementation of functions that defined in vector.h
And also it contains implementation of supporting functions.

Created by Sam
Reviewed by Micha

*/

#include <assert.h> /* assert() */
#include <string.h> /* memcpy() */
#include <stdlib.h> /* malloc(), realloc()*/

#include "vector.h"

#define GROWTH_FACTOR (2)

struct dynamic_vector
{
	void *elements;
	size_t capacity; 
	size_t element_size;
	size_t element_counter;
};

vector_t *VectorCreate(size_t capacity, size_t element_size)
{
	vector_t *new_vector = NULL;
	size_t new_vector_size = 0;
	size_t vector_t_size = 0;
	
	assert(0 < capacity);
	assert(0 < element_size);
	
	vector_t_size = sizeof(vector_t);
	new_vector = (vector_t *)malloc(vector_t_size);
	if(NULL == new_vector)
	{
		return (NULL);
	}
	
	new_vector_size = capacity * element_size;
	new_vector->elements = malloc(new_vector_size);
	if(NULL == new_vector->elements)
	{
		free(new_vector);
		new_vector = NULL;
		return (NULL);
	}
	
	new_vector->element_counter = 0;
	new_vector->capacity = capacity;
	new_vector->element_size = element_size;
	
	return(new_vector);
}

void VectorDestroy(vector_t *vector)
{
	assert(NULL != vector);
	assert(NULL != vector->elements);
	
	free(vector->elements);
	vector->elements = NULL;
	free(vector);
	vector = NULL;
}

size_t VectorSize(const vector_t *vector)
{
	assert(NULL != vector);
	return (vector->element_counter);
}

size_t VectorCapacity(const vector_t *vector)
{
	assert(NULL != vector);
	return (vector->capacity);
}

void *VectorGetElement(const vector_t *vector, size_t index)
{
	void *element = NULL;
	
	assert(NULL != vector);
	assert(vector->element_counter > index);
	
	element = (char*)vector->elements + (index * vector->element_size);
	
	return(element);
}

int VectorPushBack(vector_t *vector, const void *element)
{
	int status = 0;
	
	size_t capacity = 0;
	size_t number_existing_elements = 0;
	size_t existing_size = 0;
	
	void *destination = NULL; 
	
	assert(NULL != vector);
	assert(NULL != element);
	
	capacity = vector->capacity;
	number_existing_elements = vector->element_counter;
	
	if(capacity == number_existing_elements)
	{
		status = VectorReserve(vector, GROWTH_FACTOR * capacity);
		if(1 == status)
		{
			return (status);
		}
	}
	
	existing_size = number_existing_elements * vector->element_size;
	destination = (void *)((size_t)vector->elements + existing_size);
	memcpy(destination, element, vector->element_size);
	
	++vector->element_counter;
	
	return (status);
}

void VectorPopBack(vector_t *vector)
{
	assert(NULL != vector);
	assert(0 < vector->element_counter);
	
	--vector->element_counter;	
}

int VectorShrink(vector_t *vector)
{
	assert(NULL != vector);
	
    return VectorReserve(vector, vector->element_counter);
}

int VectorReserve(vector_t *vector, size_t new_size)
{
	void *new_alloc = NULL;
	size_t alloc_size = 0;
	
	assert(NULL != vector);
	assert(NULL != vector->elements);
	assert(vector->element_counter <= new_size);
	
	
	alloc_size = new_size * vector->element_size;
	new_alloc = realloc(vector->elements, alloc_size);
	if(NULL == new_alloc)
	{
		return(1);
	}
	
	vector->elements = new_alloc;
	vector->capacity = new_size;
	return (0);
}

