#include "ws6.h"
#include <stdio.h>/*printf*/

int main(int argc, char *argv[])
{
	int exit_status = 0;

	if (argc != 2)
	{
		printf("No second parameter \n");
		return CREATE_FILE_ERROR;
	}

	exit_status = PhaseTwo(argv[1]);

	return exit_status;
}

