#include <stdio.h> 		/* printf */
#include <stddef.h> 	/* size_t */

#define ARR_LENGTH (10)

typedef void (*func_ptr)(int);

typedef struct print_me
{
	int element;
	func_ptr print;
} print_me;


static void Print(int element)
{
	printf("element = %d\n", element);
}

void PrintMe()
{
	size_t i = 0;
	print_me arr[ARR_LENGTH];

	for(i = 0; ARR_LENGTH > i ; ++i)
	{
		arr[i].element = i;
		arr[i].print = Print;
	}
	
	for(i = 0; ARR_LENGTH > i ; ++i)
	{
		arr[i].print(arr[i].element);
	}
}



int main()
{
	PrintMe();
	return 0;
}
