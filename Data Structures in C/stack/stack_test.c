#include <stdio.h> /* printf */
#include "stack.h"

void TestStack();
stack_t *TestCreateStack();

int main()
{
    TestStack();

    return 0;
}

void PrintStars()
{
	printf("***********************************\n");
}

stack_t *TestCreateStack(stack_t *stack, const size_t capacity)
{
	stack = StackCreate(capacity, sizeof(int));
    printf("Init Stack: Capacity - %ld, ElemSize - %ld\n", capacity, sizeof(int));
    return stack;
}

void CheckOfFunction(size_t size, size_t size_test,
					 size_t capacity, size_t capacity_test, 
					 int peek, int peek_test, int IsEmpty, 
					 int IsEmpty_test, char *name)
{
	int expression1 = (size_test == size);
	int expression2 = (capacity_test == capacity);
	int expression3 = (peek_test == peek);
	int expression4 = (IsEmpty_test == IsEmpty);
	
	PrintStars();
    if(expression1 && expression2 && expression3 && expression4)
    {
        printf("%s Passed\n", name);
    }
    else
    {
        printf("%s Failed\n", name);
    }
    PrintStars();
    printf("\n");
}

void PrintValues(size_t size, size_t capacity, int peek, int IsEmpty)
{
	printf("Size: %ld\n", size);
    printf("Capacity: %ld\n", capacity);
    printf("Peek: %d\n", peek);
    printf("Is empty: %d\n", IsEmpty);
}

void CheckValues(stack_t *stack, size_t *size, size_t *capacity, int *peek, int *IsEmpty)
{    
    *size = StackSize(stack);
    *capacity = StackCapacity(stack);
    *peek = *(int *)StackPeek(stack);
    *IsEmpty = StackIsEmpty(stack);
    PrintValues(*size, *capacity, *peek, *IsEmpty);
}

void IsStackDestroyed(stack_t *stack)
{
	PrintStars();
    if(NULL != stack)
    {
        printf("Stack Destroyed\n");
    }
    else
    {
        printf("Destroy Stack Failed");
    }
    PrintStars();
}

void TestStack()
{
	int check = 5;
    int check2 = 10;    
    size_t size = 0;
    size_t capacity = 3;
    int peek = 0;
    int IsEmpty = 0;
    stack_t *stack = NULL;
    
    printf("Stack Init\n");
    stack = TestCreateStack(stack, capacity);
    CheckValues(stack, &size, &capacity, &peek, &IsEmpty);
    CheckOfFunction(size, 0, capacity, 3, peek, 0, IsEmpty, 1, "Init");
    
    printf("Push int 5 to stack\n");
    StackPush(stack, &check);
    CheckValues(stack, &size, &capacity, &peek, &IsEmpty);
    CheckOfFunction(size, 1, capacity, 3, peek, 5, IsEmpty, 0, "Push int 5");
    
    printf("Push int 10 to stack\n");
    StackPush(stack, &check2);
 	CheckValues(stack, &size, &capacity, &peek, &IsEmpty);
    CheckOfFunction(size, 2, capacity, 3, peek, 10, IsEmpty, 0, "Push int 10");

    printf("Pop element from Stack\n");
    StackPop(stack);
	CheckValues(stack, &size, &capacity, &peek, &IsEmpty);
    CheckOfFunction(size, 1, capacity, 3, peek, 5, IsEmpty, 0, "Pop from the stack");
    
    printf("Destroy Stack\n");
    StackDestroy(stack);
	IsStackDestroyed(stack);
}
