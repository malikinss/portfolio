/* Reviewed by somebody */
#ifndef __WS5_H__
#define __WS5_H__

#define NULL_SYMBOL ('\0')
#define ESCAPE (27)

typedef enum 
{ 
    OFF, 
    ON
};

int EchoOnOff(int status);
unsigned char ScanInputToUpper();
void PrintMainMenu();
int IfElseRealization();
int SwitchCaseRealization();
int LutRealization();
void PrintStars();
int ExitLoop(unsigned char useless);
void PrintInvalidInput();

#endif

