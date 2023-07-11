#include <stdio.h>	/* getchar(), printf()*/
#include <ctype.h>	/* system() */
#include <stdlib.h>	/* toupper() */ 

#include "ws5.h"

typedef int (*func_ptr)(unsigned char);
static int DoNothing(unsigned char useless);
static int PrintLetter(unsigned char key);


int IfElseRealization()
{
    unsigned char input_key = NULL_SYMBOL;
    int exit_status = OFF;
    
    PrintStars();
    printf("You chose execution via if/else");
    PrintStars();
    
    while(OFF == exit_status)
    {
    	input_key = ScanInputToUpper();
    	if (ESCAPE == input_key)
		{
			exit_status = ExitLoop(input_key);
		}
		else if ('A' == input_key || 'T' == input_key)
		{
			PrintLetter(input_key);
		}
		else
		{
			PrintInvalidInput();
		}
    }
	return (0);
}

int SwitchCaseRealization()
{
	unsigned char input_key = NULL_SYMBOL;
	int exit_status = OFF;
	
	PrintStars();
    printf("You chose execution via switch/case");
    PrintStars();
	
	while(OFF == exit_status)
	{
		input_key = ScanInputToUpper();			
		switch(input_key)
		{
			case 'A':
				PrintLetter(input_key);
				break;
				
			case 'T':
				PrintLetter(input_key);
				break;
				
			case ESCAPE:
				exit_status = ExitLoop(input_key);
				break;
				
			default:
			    PrintInvalidInput();
			    break; 
		}
	}
	return (0);
}

int LutRealization()
{
	unsigned char input_key = NULL_SYMBOL; 
	int exit_status = OFF;
	int filler = 0;
	func_ptr lut[256];

	for(filler = 0; 256 > filler; ++filler)
	{
		lut[filler] = &DoNothing;
	}
	lut[ESCAPE] = &ExitLoop;
	lut[65] = &PrintLetter;
	lut[84] = &PrintLetter;
	
	PrintStars();
    printf("You chose execution via Look Up Table (LUT)");
    PrintStars();
	
	while(OFF == exit_status)
	{	
		input_key = ScanInputToUpper();			
		exit_status = lut[input_key](input_key);
	}

	return (0);
}

int EchoOnOff(int status)
{
	int is_echo = 0;
	
	if(status)
	{
		is_echo = system("stty icanon echo");
	}
	else
	{
		is_echo = system("stty -icanon -echo");
	}
	 
	return (is_echo);	
}

void PrintMainMenu()
{	
	PrintStars();
	printf("Please, choose method of program realization:"
		"\nPress 1 to use if/else"
		"\nPress 2 to use switch/case"
		"\nPress 3 to use LUT"
		"\nPress Esc to close program (or go back)");
	PrintStars();
}

unsigned char ScanInputToUpper()
{
	unsigned char scanned_input = 0;
	scanned_input = (unsigned char) getchar();
	
	if (0 != system("clear"))
	{
		return (1);
	}
	
	return (toupper(scanned_input));	
}

int ExitLoop(unsigned char useless)
{
	(void) useless;
	return (1);
}

void PrintInvalidInput()
{
	PrintStars();
	printf("!!!!! invalid input, please try again !!!!!\n");
	printf("press ESC for Exit\n");    
	PrintStars();    
}

void PrintStars()
{
	printf("\n************************************************************\n");
}

static int DoNothing(unsigned char useless)
{
	(void) useless;
	PrintInvalidInput();
	return (0);
}

static int PrintLetter(unsigned char key)
{
	PrintStars();
	printf("you entered a %c key", key);
	PrintStars();
	return (0);
}
