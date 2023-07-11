#include <stdio.h>	/* getchar(), printf()*/

#include "ws5.h"

int TestGetKeys();

int main()
{
    return (TestGetKeys());
}

int TestGetKeys()
{
    int echo_status = 404;
    int exit_status = OFF;
    unsigned char input_key = NULL_SYMBOL;
	
    echo_status = EchoOnOff(OFF);
    
    if(0 != echo_status)
    {
		return (1);
    }
	
    while (OFF == exit_status)
    {	
		PrintMainMenu();
		input_key = ScanInputToUpper();

		switch (input_key)
		{
	    	case '1':
				IfElseRealization();
				break;
			
	    	case '2': 
				SwitchCaseRealization();
				break;
			
	    	case '3': 
				LutRealization();
				break;
			
	    	case ESCAPE:
				PrintStars();
				printf("You closed the program!");
				PrintStars();
				exit_status = ExitLoop(input_key);
				break;
			
	    	default: 
				PrintInvalidInput();
				break;
		}
    }

    echo_status = EchoOnOff(ON);
    
    if(0 != echo_status)
    {
		return (1);
    }
    
    return (0);
}
