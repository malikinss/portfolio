/*
*********************************
* Title : UID test file			*
* Author: Sam Malikin			*
* Reviewer: Micha				*
* Date : 05.05.2023				*
*********************************
*/
#include <stdio.h>	/* printf */

#include "uid.h"


int main()
{
	size_t n = 100;
	size_t i = 0;
	ilrd_uid_t test_uid1 = {0};
	ilrd_uid_t test_uid2 = {0};

	test_uid1 = UIDCreate();
	
	for(i = 0; n > i; i++)
	{
		test_uid2 = UIDCreate();
		if (UIDIsSame(test_uid1, BadUID))
		{
			printf("Sorry, UID %ld is bad.\n", i);
		}
		
		if (UIDIsSame(test_uid2, BadUID))
		{
			printf("Sorry, UID %ld is bad.\n", (i + 1));
		}

		if (UIDIsSame(test_uid1, test_uid2))
		{
			printf("Failed, UIDs are not unique.\n");
		}
		test_uid1 = test_uid2;
	}
	printf("Congrats, your UIDs are truly unique!\n");
	
	return (0);
}

