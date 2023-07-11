/* 
	Reviewed by Maxim 
	Created by Sam
*/
#include <stdio.h>	/* printf(), NULL,  */
#include <assert.h>	/*assert()*/
#include <string.h>	/* strlen(), strdup(), strcpy, */
#include <stdlib.h> /* malloc(), free() */


#include "ws8.h"

#define NUMBER_OF_ELEMENTES (3)
#define INT_VALUE (15)
#define FLOAT_VALUE (1.5)
#define STRING_VALUE ("HELLO")

#define INT_INDEX (0)
#define FLOAT_INDEX (1)
#define STRING_INDEX (2)

#define ADDITIONAL_NUMBER (50)

char *strdup(const char *s);

static int CountDigits(int num);

static int UnpackInt(void **box);
static float UnpackFloat(void **box);
static char *UnpackString(void **box);

static void *PackInt(int int_element);
static void *PackFloat(float float_element);
static void *PackString(char *string_element);

static void PrintInt(void **box);
static void PrintFloat(void **box);
static void PrintString(void **box);

static void AddInt(void **box, int x);
static void AddFloat(void **box, int x);
static void AddString(void **box, int x);

static void FreeFloatAndInt(void **box);
static void FreeString(void **box);

action_t integer_handler = {AddInt, PrintInt, FreeFloatAndInt};
action_t float_handler = {AddFloat, PrintFloat, FreeFloatAndInt};
action_t str_handler = {AddString, PrintString, FreeString};

elements_t elementes[3];

void ArrayCreater()
{
    void *box = NULL;
    void *box1 = NULL;
    void *box2 = NULL;

	box = PackInt(INT_VALUE);
	box1 = PackFloat(FLOAT_VALUE);
	box2 = PackString(STRING_VALUE);
	
    elementes[INT_INDEX].data = box;
    elementes[INT_INDEX].action = integer_handler;

    elementes[FLOAT_INDEX].data = box1;
    elementes[FLOAT_INDEX].action = float_handler;

    elementes[STRING_INDEX].data = box2;
    elementes[STRING_INDEX].action = str_handler;
    
}

void PrintAll(elements_t *elementes)
{
    size_t i;

    assert(NULL != elementes);

    for (i = 0; i < NUMBER_OF_ELEMENTES; ++i)
    {
        elementes[i].action.print(&elementes[i].data);
    }
    
    printf("\n");
}

void AddAll(elements_t *elementes)
{
    size_t i;

    assert(NULL != elementes);

    for (i = 0; i < NUMBER_OF_ELEMENTES; ++i)
    {
        elementes[i].action.add(&elementes[i].data, ADDITIONAL_NUMBER);
    }
    
    printf("\n");
}

void FreeAll(elements_t *elementes)
{
    size_t i;

    assert(NULL != elementes);

    for (i = 0; i < NUMBER_OF_ELEMENTES; ++i)
    {
        elementes[i].action.free(&elementes[i].data);
    }
    
    printf("\n");
}

void Handler()
{
    ArrayCreater();
    PrintAll(elementes);
    AddAll(elementes);
    PrintAll(elementes);
    FreeAll(elementes);
}

static int CountDigits(int num)
{  
	size_t counter = 0;
	
	assert(NULL != num);

    if (0 > num)
    {
        num = -num;
    }

    do
    {
        ++counter;
        num = num / 10;
        
    } while (0 < num);   
    
    return (counter);
}


static int UnpackInt(void **box)
{
    assert(NULL != box);
    return (*(int *)box);
}

static float UnpackFloat(void **box)
{
    assert(NULL != box);
    return (*(float *)box);
}

static char *UnpackString(void **box)
{	
	assert(NULL != box);
    return (*(char **)box);
}

static void *PackInt(int int_element)
{
    void *box = NULL;
    assert(NULL != int_element);
    *(int *)&box = int_element;
    return (box);
}

static void *PackFloat(float float_element)
{
    void *box = NULL;
    assert(NULL != float_element);
    *(float *)&box = float_element;
    return (box);
}

static void *PackString(char *string_element)
{
    void *box = NULL;
    assert(NULL != string_element);
    box = strdup(string_element);
    return (box);
}

static void PrintInt(void **box)
{
    assert(NULL != box);
    printf("Integer = %d \n", UnpackInt(box));
}

static void PrintFloat(void **box)
{
    assert(NULL != box);
    printf("Float = %f \n", UnpackFloat(box));
}

static void PrintString(void **box)
{
    assert(NULL != box);
    printf("String = %s \n", UnpackString(box));
}

static void AddInt(void **box, int x)
{
	int int_element = UnpackInt(box);
	
	assert(NULL != box);
	assert(NULL != x);
	
	int_element += x;
	*box = PackInt(int_element);
}

static void AddFloat(void **box, int x)
{
	float float_element = UnpackFloat(box);
	
	assert(NULL != box);
	assert(NULL != x);
	
	float_element += x;
	*box = PackFloat(float_element);	
}

static void AddString(void **box, int x)
{
	size_t size_of_char_element = 0;
	size_t new_size = 0;
	char *tmp_element = NULL;
	char *char_element = NULL;
	
	int size_of_digits = CountDigits(x);
	
	assert(NULL != box);
	assert(NULL != x);
	
	char_element = UnpackString(box);
	
	size_of_char_element = strlen(char_element);
	new_size = size_of_char_element + size_of_digits + 1;
	tmp_element = (char *)malloc(new_size * sizeof(char));
	
	if(NULL == tmp_element)
	{
		return;
	}
	
	strcpy(tmp_element, char_element);
	sprintf(tmp_element + size_of_char_element, "%d", x);
	
	*box = PackString(tmp_element);
	
	free(char_element);
	char_element = NULL;
	free(tmp_element);
	tmp_element = NULL;
}

static void FreeFloatAndInt(void **box)
{
	return;
	(void)box;
}

static void FreeString(void **box)
{
	char *char_element = NULL;

    assert(NULL != box);

    char_element = UnpackString(box);

    free(char_element);
    char_element = NULL;
}
