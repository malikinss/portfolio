#ifndef __STACK_H__
#define __STACK_H__

#include <stddef.h> /* size_t */

typedef struct stack stack_t;

/*
DESCRIPTION
	Creates stack of the defined capacity and element size 
	and allocates memory. Function may fail during memory
	allocation. User should be responsible for destroying stacks.
RETURN
	Function returns a pointer to a stack or NULL if it fails
	to allocate data.
INPUT
    capacity: number of elements in the stack.
    elem_size: size of a single element in bytes.
*/
stack_t *StackCreate(size_t capacity, size_t elem_size); 


/*
DESCRIPTION
	Frees the memory allocated for the stack.
RETURN
	There is no return for this function.
INPUT
    stack: a pointer to the stack.
*/
void StackDestroy(stack_t *stack);


/*
DESCRIPTION
	Removes the element from the top of the stack. Popping an empty stack 
	may cause undefined behavior.
RETURN
	There is no return for this function.
INPUT
	stack: a pointer to the stack.
*/
void StackPop(stack_t *stack);


/*
DESCRIPTION
	Adds an element to the top of the stack. The stack capaicity should not 
	be exceeded, otherwise undefined behavior is to be expected.
RETURN
	There is no return for this function.
INPUT
	stack: a pointer to the stack.
	element: a pointer to the element.
*/
void StackPush(stack_t *stack, const void *element);  

/*
DESCRIPTION
	Returns the topmost element of the stack. Peeking at empty stack may
	cause undefined behavior.
RETURN
	Pointer to the element.
INPUT
	stack: a pointer to the stack.	
*/
void *StackPeek(const stack_t *stack);

/*
DESCRIPTION
	Function returns the number of elements in the stack.
RETURN
	Number of elements in the stack.
INPUT
	stack: a pointer to the stack.
*/
size_t StackSize(const stack_t *stack);

/*
DESCRIPTION
	Checks whether the stack is empty.
RETURN
    1 - if the stack is empty.
	0 - if the stack is not empty.
INPUT
	stack: a pointer to the stack.   	
*/
int StackIsEmpty(const stack_t *stack);

/*
DESCRIPTION
	Returns the capacity of the stack.
RETURN
    Number of elements the stack can store.
INPUT
	stack: a pointer to the stack.	
*/
size_t StackCapacity(const stack_t *stack);


#endif /* __STACK_H__ */

