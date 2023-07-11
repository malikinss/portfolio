#ifndef __WS2_H__
#define __WS2_H__

void PrintAddresses();
void Swap(int *a, int *b);
void SwapSizeT(size_t *first, size_t *second);
void SwapSizeTPtr1(size_t **first, size_t **second);
void SwapSizeTPtr2(size_t **first, size_t **second);
void CopyIntArray(int *array, int *new_array, size_t size);
size_t StrLen(const char *s);
int StrCmp(const char *first_str, const char *second_str);

#endif
    
