/*

This file contains definitions of functions 
that used in vector.c and typedefs

Created by Sam

Reviewed by Micha

*/
#ifndef __VECTOR_H__
#define __VECTOR_H__

#include <stddef.h> /* size_t */

typedef struct dynamic_vector vector_t;


/*
DESCRIPTION
    Creates vector of the defined capacity and element size 
	and allocates memory. Function may fail during memory
	allocation. User should be responsible for destroying vector.
RETURN
	Function returns a pointer to a vector or NULL if it fails
	to allocate data.
INPUT
    capacity: number of elements in the vector.
    elem_size: size of a single element in bytes.
*/
vector_t *VectorCreate(size_t capacity, size_t element_size);

/*
DESCRIPTION
	Frees the memory allocated for the vector.
	User is responsible for handling dangling pointers.
RETURN
	There is no return for this function.
INPUT
    vector: a pointer to the vector.
*/
void VectorDestroy(vector_t *vector);

/*
DESCRIPTION
    Function returns the number of elements in the vector.
RETURN
    number of elements in the vector
INPUT
    vector: a pointer to the vector
*/
size_t VectorSize(const vector_t *vector);

/*
DESCRIPTION
	Function returns the current capacity of the vector.
RETURN
    Number of elements the vector can store at the moment.
INPUT
	vector: a pointer to the vector.	
*/
size_t VectorCapacity(const vector_t *vector);

/*
DESCRIPTION
    Function returns the element at index. Trying to access the index
    that exceeds the vector size may result in undefined behavior.
RETURN
    A pointer to the element.
INPUT
    vector: a pointer to vector
    index: index of an element
*/
void *VectorGetElement(const vector_t *vector, size_t index);


/*
DESCRIPTION
    Adds an element to the end of the vector. If the element is larger than 
    the element size of the vector it will be truncated.
    Resizes the vector if it reaches capacity. Function may fail to resize 
    the vector.
RETURN
    0 - adding an element is successful;
    1 - adding an element is not succeful.
INPUT
    Vector pointer and an element the user wants to add.
*/
int VectorPushBack(vector_t *vector, const void *element);

/*
DESCRIPTION
    Removes the element from the end of the vector. Trying to remove the element 
    from the empty vector may result in underfinded behavior.
RETURN
	There is no return for this function.
INPUT
    vector: a pointer to the vector.
*/
void VectorPopBack(vector_t *vector);

/*
DESCRIPTION
    Reeduces the capacity of the vector to the current size
    Reallocation of memory may fail.
RETURN
    0 - reallocation is successful;
    1 - reallocation is not succeful.
INPUT
    vector: pointer to function;
    new_size: new size of vector.
*/
int VectorShrink(vector_t *vector); 

/*
DESCRIPTION
    Expands the capacity of the vector according to the user's needs.
    Reallocation of memory may fail.
RETURN
    0 - reallocation is successful;
    1 - reallocation is not succeful.
INPUT
    vector: pointer to function;
    new_size: new size of vector.
*/
int VectorReserve(vector_t *vector, size_t new_size); 

#endif /* __VECTOR_H__ */


