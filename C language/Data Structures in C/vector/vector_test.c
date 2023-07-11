/*

This file contains functions for testing functions that defined in vector.h

Created by Sam
Reviewed by Micha

*/

#include <stdio.h>	/* printf */
#include "vector.h"

int main()
{
	vector_t *test_vector = NULL;
	size_t capacity = 2;
	size_t element_size = 4;
	int elem_1 = 5;
	float elem_2 = 3.0;
	int *test_get = NULL;
	float *test_get2 = NULL;
	
	test_vector = VectorCreate(capacity, element_size);	
	printf("Vector created! Let's test it!\n\n");


	printf("Testing VectorCapacity...\n");
	if (capacity != VectorCapacity(test_vector))
	{
		printf("Failed :(\n");
	}
	printf("Done!\n\n");

	printf("Testing VectorPushBack, VectorGetElement and VectorSize...\n");
	VectorPushBack(test_vector, &elem_1);
	VectorPushBack(test_vector, &elem_2);	
	test_get = (int *)VectorGetElement(test_vector, 0);
	if (*test_get != elem_1)
	{
		printf("Failed with element 1 :(\n");
	}
	test_get2 = (float *)VectorGetElement(test_vector, 1);
	if (*test_get2 != elem_2)
	{
		printf("Failed with element 2 :(\n");
	}	
	if (2 != VectorSize(test_vector))
	{
		printf("Failed :(\n");
	}
	printf("Done!\n\n");

	printf("Testing VectorPushBack with resize...\n");
	VectorPushBack(test_vector, &elem_1);
	if (3 != VectorSize(test_vector))
	{
		printf("Failed :(\n");
	}
	printf("Done!\n\n");
	test_get = (int *)VectorGetElement(test_vector, 2);
	if (*test_get != elem_1)
	{
		printf("Failed with element 1 :(\n");
	}

	printf("Testing VectorPopBack...\n");
	VectorPopBack(test_vector);
	if (2 != VectorSize(test_vector))
	{
		printf("Failed :(\n");
	}
	VectorPushBack(test_vector, &elem_1);
	if (3 != VectorSize(test_vector))
	{
		printf("Failed :(\n");
	}
	test_get = (int *)VectorGetElement(test_vector, 2);
	if (*test_get != elem_1)
	{
		printf("Failed :(\n");
	}
	printf("Done!\n\n");	

	printf("Testing VectorReserve...\n");
	VectorReserve(test_vector, 8);
	if (8 != VectorCapacity(test_vector))
	{
		printf("Failed :(\n");
	}
	printf("Done!\n\n");

	printf("Testing VectorShrink...\n");
	VectorShrink(test_vector);
	if (VectorSize(test_vector) != VectorCapacity(test_vector))
	{
		printf("Failed :(\n");
	}
	VectorPushBack(test_vector, &elem_1);
	if (VectorSize(test_vector) == VectorCapacity(test_vector))
	{
		printf("Failed :(\n");
	}
	test_get = (int *)VectorGetElement(test_vector, 0);
	if (*test_get != elem_1)
	{
		printf("Failed :(\n");
	}
	test_get = (int *)VectorGetElement(test_vector, 3);
	if (*test_get != elem_1)
	{
		printf("Failed :(\n");
	}
	printf("Done!\n\n");

	VectorDestroy(test_vector);
	test_vector = NULL;
	printf("The vector is gone! Check for leaks with Valgrind :)\n\n");


	return (0);
}

