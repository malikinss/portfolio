#include <string.h> /* memcpy */
#include <stdlib.h> /* malloc free*/
#include <assert.h>

#include "stack.h"

#define STACK_T_SIZE sizeof(stack_t);

struct stack
{
    void *elements;
    void *top;
    size_t capacity;
    size_t elem_size;

};


stack_t *StackCreate(size_t capacity, size_t elem_size)
{
	stack_t *stack = NULL;
	size_t stack_t_size = 0;
	size_t stack_max_size = 0;
	
	assert(0 != capacity);
    assert(0 != elem_size);
    
    stack_t_size = sizeof(stack_t);
    stack_max_size =  capacity * elem_size;
    
    stack = (stack_t *)malloc(stack_t_size + stack_max_size);
    if(NULL == stack)
    {
    	return NULL;
    }

	stack->elements = stack + 1;
	stack->top = stack->elements;
	
    stack->capacity = capacity;
    stack->elem_size = elem_size;

	return stack;
}

void StackDestroy(stack_t *stack)
{

    assert(NULL != stack);

    free(stack);
    stack = NULL;
}

void StackPop(stack_t *stack)
{
    size_t elem_size = 0;
    size_t top = 0;
    
    assert(NULL != stack);
    assert(NULL != stack->top);
    
    elem_size = stack->elem_size;
    top = (size_t)stack->top;

    stack->top = (void *)(top - elem_size);
}

void StackPush(stack_t *stack, const void *element)
{
    size_t elem_size = 0;
    size_t top = 0;
    
    assert(NULL != stack);
    assert(NULL != element);

    memcpy(stack->top, element, stack->elem_size);
    
    elem_size = stack->elem_size;
    top = (size_t)stack->top;
    stack->top = (void *)(top+ elem_size);
}

void *StackPeek(const stack_t *stack)
{	
	size_t elem_size = 0;
    size_t top = 0;
    
    assert(NULL != stack);
    
    elem_size = stack->elem_size;
    top = (size_t)stack->top;
    
    return (void *)(top - elem_size);
}

size_t StackSize(const stack_t *stack)
{
    size_t elem_size = 0;
    size_t top = 0;
    size_t elements = 0;

    assert(NULL != stack);
    
    elem_size = stack->elem_size;
    top = (size_t)stack->top;
    elements = (size_t)stack->elements;

    return (top - elements) / elem_size;
}

int StackIsEmpty(const stack_t *stack)
{
    size_t top = 0;
    size_t elements = 0;

    assert(NULL != stack);
    
    top = (size_t)stack->top;
    elements = (size_t)stack->elements;

    return (0 == top - elements);
}

size_t StackCapacity(const stack_t *stack)
{
    assert(NULL != stack);

    return stack->capacity;
}
