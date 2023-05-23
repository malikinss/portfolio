/* 
	Reviewed by Maxim 
	Created by Sam
*/
#ifndef __WS8_H__
#define __WS8_H__

typedef void (*action_add_t)(void **box, const int x);
typedef void (*action_print_t)(void **box);
typedef void (*action_free_t)(void **box);

typedef struct actions
{
    action_add_t add;
    action_print_t print;
    action_free_t free;
} action_t;

typedef struct element
{
    void *data;
    action_t action;
} elements_t;

void Handler();
void ArrayCreater();
void PrintAll(elements_t *elementes);
void AddAll(elements_t *elementes);
void FreeAll(elements_t *elementes);

#endif	/* __WS8_H__ */
