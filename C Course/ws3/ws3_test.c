#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include "ws3.h" 
 
void TestStrCpy();
void TestStrNCpy();
void TestStrNCmp();
void TestStrCaseCmp();
void TestStrChr();
void TestStrDup();
void TestStrCat();
void TestStrNCat();
void TestStrStr();
void TestStrSpn();
void TestIsPalindrome();
char *strdup(const char *s);
int strcasecmp(const char *s1, const char *s2);

int main()
{
    TestStrCpy();
    TestStrNCpy();
    TestStrNCmp();
    TestStrCaseCmp();
    TestStrChr();
    TestStrDup();
    TestStrCat();
    TestStrNCat();
    TestStrStr();
    TestStrSpn();
    TestIsPalindrome();

    return (0);
}

void PassOrFail(const int expression, const char *name)
{
 	printf("************ Test of %s ************\n", name);
 	if(expression)
    {
    	puts("Passed\n");
    }
    else
    {
    	puts("Failed\n");
    }
}

void TestStrCpy()
{   
    char src_s[20] = "Hello World!";
    char str1[20];
    char str2[20];

    char *test1 = strcpy(str1, src_s);
    char *test2 = StrCpy(str2, src_s);

    int expression = (0 == strcmp(test1, test2)); 
    PassOrFail(expression, "StrCpy");
}

void TestStrNCpy()
{   
    char src_s[20] = "Shalom LeKulam!";
    char str1[20];
    char str2[20];
    size_t n = 4;
    
    char *test1 = strncpy(str1, src_s, n);
    char *test2 = StrNCpy(str2, src_s, n);
    
    int expression = (0 == strcmp(test1, test2)); 
    PassOrFail(expression, "StrNCpy");
}

void TestStrNCmp()
{   
    char str1[20] = "Hello World!";
    char str2[20] = "Hello World!";
    char str3[20] = "HeLlo World!";

    int test_StrNCmp1 = StrNCmp(str1 , str2, 11);
    int test_StrNCmp2 = StrNCmp(str1 , str2, 2);
    int test_StrNCmp3 = StrNCmp(str2 , str3, 11);
    int test_StrNCmp4 = StrNCmp(str2 , str3, 4);
    
    int test_strncmp1 = strncmp(str1 , str2, 11);
    int test_strncmp2 = strncmp(str1 , str2, 2);
    int test_strncmp3 = strncmp(str2 , str3, 11);
    int test_strncmp4 = strncmp(str2 , str3, 4);
    
    int case1 = (test_StrNCmp1 == test_strncmp1); 
    int case2 = (test_StrNCmp2 == test_strncmp2); 
    int case3 = (test_StrNCmp3 == test_strncmp3);
    int case4 = (test_StrNCmp4 == test_strncmp4);
    int expression = (case1 && case2 && case3 && case4); 

    PassOrFail(expression, "StrNCmp");
}

void TestStrCaseCmp()
{
    char* s1 = "Geeks";
    char* s2 = "geeks";
    char* s3 = "Geeks!";
    char* s4 = "Gmeks";
        
    int strcmp_t1 = strcasecmp(s1, s2);
    int strcmp_t2 = strcasecmp(s2, s3);
    int strcmp_t3 = strcasecmp(s3, s4);
        
    int test_cmp1 = StrCaseCmp(s1, s2);
    int test_cmp2 = StrCaseCmp(s2, s3);
    int test_cmp3 = StrCaseCmp(s3, s4);


    int case1 = (strcmp_t1 == test_cmp1); 
    int case2 = (strcmp_t2 == test_cmp2); 
    int case3 = (strcmp_t3 == test_cmp3);
    int expression = (case1 && case2 && case3); 

    PassOrFail(expression, "StrCaseCmp");
}

void TestStrChr()
{
    char *s1 = "Geeks";
    int ch1 = 'e';
    int ch2 = 'm';
  
    char *strchr_t1 = strchr(s1, ch1);
    char *strchr_t2 = strchr(s1, ch2);
        
    char *test_chr1 = StrChr(s1, ch1);
    char *test_chr2 = StrChr(s1, ch2);
    
    int case1 = (strchr_t1 == test_chr1); 
    int case2 = (strchr_t2 == test_chr2);
    int expression = (case1 && case2); 

    PassOrFail(expression, "StrChr");
}

void TestStrDup()
{
    char *s1 = "Hello World!";
    char *s2 = "Eurika!";
		
    char *strdup_t1 = strdup((char *)s1);
    char *strdup_t2 = strdup((char *)s2);
        
    char *test_dup1 = StrDup(s1);
    char *test_dup2 = StrDup(s2);
    
    int case1 = (!strcmp(strdup_t1, test_dup1)); 
    int case2 = (!strcmp(strdup_t2, test_dup2));
    int expression = (case1 && case2); 

    PassOrFail(expression, "StrDup");	
}

void TestStrCat()
{
    char s1[50] = "Hello World!";
    char s2[50] = "Eurika!";
		
    char *strcat_t1 = strcat(s1, s2);      
    char *test_cat1 = StrCat(s1, s2);

    int expression = (!strcmp(strcat_t1, test_cat1)); 

    PassOrFail(expression, "StrCat");	
}

void TestStrNCat()
{
    char s1[50] = "Hello World!";
    char s2[50] = "Eurika!";
		
    char *strncat_t1 = strncat(s1, s2, 5);      
    char *test_ncat1 = StrNCat(s1, s2, 5);
    
    int expression = (!strcmp(strncat_t1, test_ncat1)); 

    PassOrFail(expression, "StrNCat");
}

void TestStrStr()
{	
    char *needle = "on";
    char *haystack= "Helmonleon";
		
    char *strstr_t1 = strstr(haystack, needle);      
    char *test_strstr1 = StrStr(haystack, needle);
    
    int expression = (!strcmp(strstr_t1, test_strstr1)); 

    PassOrFail(expression, "StrStr");
}

void TestStrSpn()
{
    const char *s = "lo World";
    const char *accept = "kjcedkjsnwn lkjdsrzaUGUIWGH";
		
    char strspn_t1 = strspn(s, accept);      
    char test_spn1 = StrSpn(s, accept);
	int expression = (strspn_t1 == test_spn1); 

    PassOrFail(expression, "StrSpn");	
}

void TestIsPalindrome()
{
    const char *s1 = "TEET";
    const char *s2 = "TEnET";
    const char *s3 = "TEeT";
    const char *s4 = "TEneT";
    
    int res1 = IsPalindrome(s1);
    int res2 = IsPalindrome(s2);
    int res3 = IsPalindrome(s3);
    int res4 = IsPalindrome(s4);

    int case1 = (0 == res1); 
    int case2 = (0 == res2);
    int case3 = (1 == res3);
    int case4 = (1 == res4);     
    
    int expression = (case1 && case2 && case3 && case4); 

    PassOrFail(expression, "IsPalindrome");
}

