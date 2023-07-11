#include <assert.h> 	/* assert */
#include <stdio.h> 		/* assert */
#include <string.h>		/* strcpy */
#include <stdlib.h>		/* malloc */
#include <ctype.h>		/* tolower */
#include "ws3.h"

#define NULL_TERMINATOR ('\0')

char *StrCpy(char *dest, const char *src)
{
    char *runner = dest;
    
    assert(NULL != dest);
    assert(NULL != src);
		
    while(NULL_TERMINATOR != *src)
    {
		*runner = *src;
		++runner;
		++src;
    }
    *runner = NULL_TERMINATOR;
    return (dest);   
}

char *StrNCpy(char *dest, const char *src, size_t n)
{
    const char *end_dest = dest + n;
    const char *end_src = src + n;
    char *runner_dest = dest;
    
    assert(NULL != dest);
    assert(NULL != src);
		
    while(end_src != src && NULL_TERMINATOR != *src)
    {
		*runner_dest = *src;
		++runner_dest;
		++src;
    }
    while(end_dest != runner_dest)
    {
		*runner_dest  = NULL_TERMINATOR;
		++runner_dest;
    }
    return (dest);    
}

int StrNCmp(const char *s1, const char *s2, size_t n)
{ 
    const char *runner1 = s1;
    const char *runner2 = s2;

    assert(NULL != s1);
    assert(NULL != s2);

    while(*runner1 == *runner2 && NULL_TERMINATOR != *runner2 && (s1 + n) != runner1)
    {
        ++runner1;
        ++runner2;
    }
    return ((int) *runner1 - *runner2);
}

int StrCaseCmp(const char *s1, const char *s2)
{
	const char *runner1 = s1;
	const char *runner2 = s2;	
	
    assert(NULL != s1);
    assert(NULL != s2);
        
    while(tolower(*runner1) == tolower(*runner2) && NULL_TERMINATOR != *runner2)
    {
		++runner1;
        ++runner2;
    }    
    return ((int) tolower(*runner1) - tolower(*runner2));
}

char *StrChr(const char *s, int c)
{   
    char *runner = (char *)s;
	char check = c;
	    
    assert(NULL != s);
    assert(NULL != c);
    
    do 
	{
		if (check == *runner)
		{
			return (runner);
		}
	} while (NULL_TERMINATOR != *runner++);
	return (NULL);
}

char *StrDup(const char *s)
{
    size_t s_len = strlen(s);
    char *dup_s = (char *)malloc(s_len * sizeof(dup_s));

    assert(s != NULL);

    if(NULL == dup_s)
    {
        printf("Error of duplication\n");
        return (char *)NULL;
    }
    strcpy(dup_s, s);
    return (dup_s);
}

char *StrCat(char *dest, const char *src)
{
    char *end_d = dest + strlen(dest);
    
    assert(NULL != dest);
    assert(NULL != src);
        
    strcpy(end_d, src);
    end_d += strlen(src); 
    *end_d = NULL_TERMINATOR;
        
    return dest;
}

char *StrNCat(char *dest, const char *src, size_t n)
{
    char *end_d = dest + strlen(dest);
    
    assert(NULL != dest);
    assert(NULL != src);
    assert(NULL != n);
    
    strncpy(end_d, src, n);
    end_d = end_d + n;    
    *end_d = NULL_TERMINATOR;
        
    return dest;
}

char *StrStr(const char *haystack, const char *needle)
{   
    size_t len_of_needle = strlen(needle);
	char *runner = (char *) haystack;

	assert(NULL != haystack);
	assert(NULL != needle);

	while(NULL_TERMINATOR != *runner)
    {
        if(*runner == *needle && 0 == strncmp(runner, needle, len_of_needle))
        {
            break;
        }
        ++runner;
    }
    if(NULL_TERMINATOR == *runner)
    {
        runner = NULL;
    }
    return (runner);
}

size_t StrSpn(const char *s, const char *accept)
{
    char *runner = (char *)s;
	
	assert(NULL != s);
	assert(NULL != accept);

	while(NULL != strchr(accept, *runner) && NULL_TERMINATOR != *runner)
	{
		++runner;
	}
	return ((size_t)(runner - s));
}

int IsPalindrome(const char *s)
{
    const char *start = s;
    const char *end = NULL;
    
    assert(NULL != s);
    
    end = start + strlen(s) - 1;
	while(end >= start)
	{
		if(*start != *end)
		{
			return (1);
		}
		++start;
		--end;
	}
	return (0);
}
