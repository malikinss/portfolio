/* Reviewed by Dima */
#ifndef __WS4_H__
#define __WS4_H__

#include <stddef.h> /* size_t */

int *SumOfMatrixRows(int **arr, size_t row, size_t col, int *result);
void CreateArray(int **arr, size_t row, size_t col);
void PrintArray(int *result, size_t row);
void FreeAllInt(int **arr, size_t size);

void InitSoldiersArray(unsigned int *soldiers, size_t n);
unsigned int FindLastSurvivor(unsigned int *soldiers);
unsigned int JosephusProblem(const size_t n);

void PrintDataTypes();

size_t EnvLength(char **envp);
char *DuplicateToLower(const char *s);
void FreeAll(char **buffer, size_t length);
void PrintAll(char **buffer, char **envp);
void CpyEvnpVars(char **buffer, char **envp);
void EnvpVar(char **envp);

#endif

