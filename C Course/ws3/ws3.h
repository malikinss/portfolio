#ifndef __WS3_H__
#define __WS3_H__

#include <stddef.h> /* size_t */

/*DESCRIPTION:
    The  StrCpy() function  copies  the  string pointed to by src, including
    the terminating null byte ('\0'), to the buffer pointed to by dest. The 
    strings may not overlap, and the destination string dest must be large
    enough to receive the copy. Beware of buffer overruns!
    
    The  StrNCpy()  function  is  similar,  except that at most n bytes of src
    are copied. Warning: If there is no null byte among the first n bytes of 
    src, the string placed in dest will not be null-terminated.
    
    If the length of src is less than n, StrNCpy() writes additional null 
    bytes to dest to ensure that a total of n bytes are written.
       
PARAMS:
    dest:   Pointer to buffer to copy to.
    src:    Pointer to const string to copy.
    n:      The number of characters to be copied from source.
         
RETURN:
    Returns a pointer to the beginning of dest string.
*/
char *StrCpy(char *dest, const char *src);
char *StrNCpy(char *dest, const char *src, size_t n);

/*DESCRIPTION
    The  StrNCmp() function compares only the first (at most) n bytes
    of s1 and s2. The comparison is done using unsigned characters.
    StrNCmp() returns an integer indicating the result of the
    comparison, as follows:

   • 0, if the s1 and s2 are equal;
   • a negative value if s1 is less than s2;
   • a positive value if s1 is greater than s2.

RETURN:
    if Return value < 0 then it indicates str1 is less than str2.
    if Return value > 0 then it indicates str2 is less than str1.
    if Return value = 0 then it indicates str1 is equal to str2.
       
PARAMS:
    str1 − This is the first string to be compared.
    str2 − This is the second string to be compared.
    n − The maximum number of characters to be compared.
*/
int StrNCmp(const char *s1, const char *s2, size_t n);

/*DESCRIPTION
    The  StrCaseCmp() function performs a byte-by-byte comparison of the
    strings s1 and s2, ignoring the case of the characters. It returns 
    an integer less than, equal to, or greater than zero if s1 is found,
    respectively, to be less than, to match, or be greater than s2.

RETURN:
    The  StrCaseCmp() function return an integer less than, equal to,
    or greater than zero if s1 is, after ignoring case, found to be less than,
    to match, or be greater than s2, respectively.

PARAMS:
    str1 − This is the first string to be compared.
    str2 − This is the second string to be compared.
*/
int StrCaseCmp(const char *s1, const char *s2);

/*DESCRIPTION
   The StrChr() function returns a pointer to the first occurrence of 
   the character c in the string s.

RETURN:
   This returns a pointer to the first occurrence of the character c in the
   string str, or NULL if the character is not found.
  
PARAMS:
    s − This is the C string to be scanned.
    c − This is the character to be searched in str.
*/
char *StrChr(const char *s, int c);

/*DESCRIPTION
    The  StrDup() function returns a pointer to a new string which is a 
    duplicate of the string s. Memory for the new string is obtained with 
    malloc(), and can be freed with free().

RETURN:
    On success, the StrDup() function returns a pointer to the duplicated
    string. It returns NULL if insufficient memory was available.
    
PARAMS:
    s − String to be dublicated
*/
char *StrDup(const char *s);

/*DESCRIPTION
    The  StrCat() function appends the src string to the dest string,
    overwriting the terminating null byte ('\0') at the end of dest, and then
    adds a terminating null byte.  The strings may not overlap, and the dest
    string must have enough space for the result. If dest is not large 
    enough, program behavior is unpredictable; buffer overruns are a favorite
    avenue for attacking secure programs.
    The StrNCat() function is similar, except that
    *  it will use at most n bytes from src;
    *  src does not need to be null-terminated if it contains n or more bytes.
    As with StrCat(), the resulting string in dest is always null-terminated.
    If src contains n or more bytes, StrNCat() writes n+1 bytes to dest
    (n from src plus the terminating null byte).  
    There‐fore, the size of dest must be at least strlen(dest)+n+1.

RETURN:
    This function returns a pointer to the resulting string dest.
    
PARAMS:
    dest − This is pointer to the destination array, which should contain
    a C string, and should be large enough to contain the concatenated
    resulting string. src − This is the string to be appended. This should
    not overlap the destination.
*/
char *StrCat(char *dest, const char *src);
char *StrNCat(char *dest, const char *src, size_t n);

/*DESCRIPTION:
    The  StrStr() function finds the first occurrence of the substring
    needle in the string haystack. The terminating null bytes ('\0')
    are not compared.
       
PARAMS:
    needle:       Pointer to string to find.
    haystack:     Ponter to string where to search for needle.
         
RETURN:
    These function return a pointer to the beginning of the located
    sub‐string, or NULL if the substring is not found.

*/
char *StrStr(const char *haystack, const char *needle);

/*DESCRIPTION
    The  StrSpn()  function calculates the length (in bytes) of the initial
    segment of s which consists entirely of bytes in accept.

PARAMS:
    s − Pointer to string to be scanned.
    accept − Pointer to string containing the characters to match.
    
RETURN:
    The  StrSpn() function returns the number of bytes in the initial seg‐
    ment of s which consist only of bytes from accept.
    
*/
size_t StrSpn(const char *s, const char *accept);

/*DESCRIPTION
    Function IsPalindrome() checks if string is a palidrome (could include
    all characters).

RETURN:
    Function returns 0 if string is a palindrome.
    Function returns 1 if string is not a palindrome.
    
PARAMS:
    s - string that is being checked.
*/
int IsPalindrome(const char *s);

/*DESCRIPTION
    Function Boom() recieves a range of numbers and prints all of them,
    except the numbers that contain a 7 digit or are divisible by 7.
    Instead of those numbers the function prints "BOOM".

RETURN:
    Function does not return anything
    
PARAMS:
    from:   Starting number of the range.
    to:     Ending number of the range.
*/
void Boom(int from, int to); 

/*DESCRIPTION
    Function RemoveSpaces() receives a string and removes redundant
    white spaces:
    - spaces and tabulation in the beginning and the end of string;
    - duplicate spaces within the string (keeping the first white
    space in a sequence).

RETURN:
    function returns a pointer to a beginning of a modified string.
    
PARAMS:
    s:      String that will be modified.
*/
char *RemoveSpaces(char *s);

#endif /* __WS3_H__ */
