#include <stdio.h> 		/*printf*/
#include <stdlib.h> 	/* malloc, free */
#include <stddef.h> 	/*FILE*/
#include <string.h> 	/* strcpy */
#include <assert.h> 	/* assert */

#include "ws9.h"    	/* my header file  */

static status_t Check(int expression, status_t if_true, status_t if_false);

status_t OpenNCheckFile(FILE **fptr, char *filename, const char *operation)
{
	int expression = 0;
	
	assert(NULL != operation);
	assert(NULL != filename);
	
	*fptr = fopen(filename, operation);
	
	expression = (NULL == fptr);
	
	return (Check(expression, OPEN_ERROR, SUCCESS));
}

status_t CloseNCheckFile(FILE **fptr)
{
	int expression = 0;
	
	assert(NULL != *fptr);
	
	expression = (EOF == fclose(*fptr));
	
	return (Check(expression, CLOSE_ERROR, SUCCESS));
}

status_t WriteNCheckFile(FILE **fptr, size_t size, student_grades *grades)
{
	int expression = 0;
	
	size_t num_elements = 0;
	
	assert(NULL != *fptr);
	assert(0 != size);
	assert(NULL != grades);
	
	num_elements = fwrite(grades, size, 1, *fptr);
	
	expression = (1 != num_elements);
	
	return (Check(expression, WRITE_ERROR, SUCCESS));
}

status_t ReadNCheckFile(FILE **fptr, size_t size, student_grades *grades)
{
	size_t num_elements = 0;
	
	int expression = 0;
	
	assert(NULL != *fptr);
	assert(0 != size);
	assert(NULL != grades);
	
    num_elements = fread(grades, size, 1, *fptr);
    
    expression = (1 != num_elements);
	
	return (Check(expression, READ_ERROR, SUCCESS));
}

status_t MakeFileName(char *last_name, char **filename)
{
	char *filename_end = ".bin";
	char *end_of_filename = NULL;
	
	size_t len_last_name = 0; 
	size_t len_filename_end = 0;
	size_t len_filename = 0;
	size_t char_size = 0;
	
	assert(NULL != last_name);
	
	char_size = sizeof(char);
	
	len_last_name = strlen(last_name);
	len_filename_end = strlen(filename_end);
	
	len_filename = len_last_name + len_filename_end + 1;
	
	*filename = (char *)malloc(len_filename * char_size);
	
    if (NULL == *filename)
    {
        return (MEM_ALLOC_ERROR);
    }
    
    strcpy(*filename, last_name);
    
    end_of_filename = *filename + len_last_name * char_size;
    
	sprintf(end_of_filename, "%s", filename_end);
	
	return (SUCCESS);
}

status_t SaveRecord(student_grades *grades)
{
	char *filename = NULL; 
	status_t ret_status = SUCCESS;

	FILE *fptr = NULL;
	
	assert(NULL != grades);
	
	MakeFileName(grades -> last_name, &filename);
		
	ret_status = OpenNCheckFile(&fptr, filename, "w");
	if(SUCCESS != ret_status)
	{
		free(filename);
    	filename = NULL;
		return (ret_status);
	}
	
	ret_status = WriteNCheckFile(&fptr, sizeof(*grades), grades);
	if(SUCCESS != ret_status)
	{
		free(filename);
    	filename = NULL;
		return (ret_status);
	}
    
    ret_status = CloseNCheckFile(&fptr);
    
    free(filename);
    filename = NULL;
    
	return (ret_status);
}

status_t LoadRecord(student_grades *grades, char *filename)
{
	FILE *fptr = NULL;
	status_t ret_status = SUCCESS;

    assert(NULL != grades);
    assert(NULL != filename);

    ret_status = OpenNCheckFile(&fptr, filename, "r");
    if(SUCCESS != ret_status)
	{
		return (ret_status);
	}
	
	ret_status = ReadNCheckFile(&fptr, sizeof(*grades), grades);
	if(SUCCESS != ret_status)
	{
		return (ret_status);
	}
	
    ret_status = CloseNCheckFile(&fptr);

    return (ret_status);
}

static status_t Check(int expression, status_t if_true, status_t if_false)
{
	if(expression)
	{
		return (if_true);
	}
	else
	{
		return (if_false);
	}	
}
