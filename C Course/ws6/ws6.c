#include <stdio.h>	/* printf, fopen, FILE, fgets,remove, fgetc, 
						fclose, fread, fseek, fprintf, fwrite, fputs */
#include <stddef.h>	/* size_t */
#include <assert.h>	/* assert */
#include <string.h>	/* strlen, strcmp, strncmp */

#include "ws6.h"

#define MAX_STRING (1024)
#define CHAIN_LENGTH (sizeof(handlers) / sizeof(*handlers))

static const handlers_t handlers[] = {
	{"-exit\n", strcmp, Exit},
	{"-remove\n", strcmp, RemoveFile},
	{"-count\n", strcmp, CountStrFile},
	{"<", CompareFirstChar, AddToBegining},
	{NULL, DefaultValue, AddToEndFile}};

static status_t RetStatus(int expression, status_t if_true, status_t if_false);
static status_t IsFileOpen(FILE *fptr);
static status_t IsWrited(int write_status);
static status_t IsReaded(const char *input);
static status_t IsFileClosed(int close_status);
static status_t WriteNCheck(char *write_string, FILE *fptr);
static status_t ReadNCheck(char *read_string, FILE *fptr);
static status_t CloseNCheck(FILE *fptr);
static FILE *OpenNCheck(const char *file_name, const char *option, FILE *fptr, status_t *ret_status);
static status_t ReNameFile(const char *old_file, const char *new_file);


status_t AddToBegining(const char *file_name, char *write_string)
{
	FILE *fptr_new = NULL;
	FILE *fptr_old = NULL;
	
	status_t ret_status = SUCCESS;
	char *read_status = " ";
	char *new_file_name = "newfile.txt";
	char read_string[MAX_STRING] = " ";
	const char *old_file_name = file_name;
	
	++write_string;
	
	fptr_old = OpenNCheck(old_file_name, "r", fptr_old, &ret_status);
	fptr_new = OpenNCheck(new_file_name, "w", fptr_new, &ret_status);
	
	ret_status = WriteNCheck(write_string, fptr_new);
	
	do
	{
		ret_status = ReadNCheck(read_string, fptr_old);
		
		if(ret_status == READ_ERROR)
		{
			break;
		}
		
		ret_status = WriteNCheck(read_string, fptr_new);
	}while(NULL != read_status);
	
	ret_status = CloseNCheck(fptr_old);
	ret_status = CloseNCheck(fptr_new);
	ret_status = ReNameFile(old_file_name, new_file_name);
	return (ret_status);
}

status_t AddToEndFile(const char *file_name, char *write_string)
{
	FILE *fptr = NULL;
	status_t ret_status = SUCCESS;
	fptr = OpenNCheck(file_name, "a", fptr, &ret_status);
	ret_status = WriteNCheck(write_string, fptr);
	ret_status = CloseNCheck(fptr);
	return (ret_status);
}

status_t CountStrFile(const char *file_name, char *user_input)
{
	FILE *fptr = NULL;
	size_t count = 0;
	char read_string[MAX_STRING] = {0};
	status_t ret_status = SUCCESS;

	assert(NULL != file_name);
	assert(NULL != user_input);

	fptr = OpenNCheck(file_name, "r", fptr, &ret_status);

	while(ret_status == ReadNCheck(read_string, fptr))
	{
		++count;
	}

    printf("File %s has %ld lines\n", file_name, count);

	return (ret_status);
	(void) user_input;	
}


status_t ChainOfResponsibility(const char *filename, char *user_input)
{
	size_t i = 0;
	status_t ret_status = SUCCESS;
	
	for(i = 0; CHAIN_LENGTH > i; ++i)
	{
		comp_ptr_t comparison_func = handlers[i].comparison;
		act_ptr_t operation_func = handlers[i].operation;
		const char *command_input = handlers[i].command;

		if (0 == comparison_func(user_input, command_input))
		{
			ret_status = operation_func(filename, user_input);
			i = 5;
			return ret_status;
		}
	}
	return (ret_status);
}

int PhaseTwo(const char *filename)
{
	char *input_status = 0;
	char input_string[MAX_STRING];
	status_t ret_status = SUCCESS;

	while (SUCCESS == ret_status)
	{
		input_status = fgets(input_string, MAX_STRING, stdin);
		ret_status = IsReaded(input_status);
		ret_status = ChainOfResponsibility(filename, input_status);
	}
	
	return (ret_status);
}

status_t Exit(const char *filename, char *dummy)
{
	return (EXIT_BY_USER);
	(void)filename;
	(void)dummy;
}

status_t RemoveFile(const char *filename, char *dummy)
{
	int expression = (0 == remove(filename)); 
	return (RetStatus(expression, SUCCESS, DELETE_ERROR));
	(void)dummy;
}

int CompareFirstChar(const char *input_string, const char *command)
{
	return (strncmp(input_string, command, 1));
}

int DefaultValue()
{
	return (0);
}

static status_t RetStatus(int expression, status_t if_true, status_t if_false)
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

static status_t IsFileOpen(FILE *fptr)
{
	int expression = (NULL == fptr); 
	return (RetStatus(expression, OPEN_ERROR, SUCCESS));	
}

static status_t IsWrited(int write_status)
{
	int expression = (EOF == write_status); 
	return (RetStatus(expression, WRITE_ERROR, SUCCESS));
}

static status_t IsReaded(const char *input)
{
	int expression = (NULL == input); 
	return (RetStatus(expression, READ_ERROR, SUCCESS));	
}

static status_t IsFileClosed(int close_status)
{
	int expression = (0 != close_status); 
	return (RetStatus(expression, CLOSE_ERROR, SUCCESS));	
}

static status_t WriteNCheck(char *write_string, FILE *fptr)
{
	status_t write_status = fputs(write_string, fptr);
	return (IsWrited(write_status));
}

static status_t ReadNCheck(char *read_string, FILE *fptr)
{
	char *read_status = fgets(read_string, MAX_STRING, fptr);
	return (IsReaded(read_status));
}

static status_t CloseNCheck(FILE *fptr)
{
	int close_status = fclose(fptr); 
	return (IsFileClosed(close_status));
}

static FILE *OpenNCheck(const char *file_name, const char *option, FILE *fptr, status_t *ret_status)
{
	fptr = fopen(file_name, option);
	*ret_status = IsFileOpen(fptr);
	return (fptr);
}

static status_t ReNameFile(const char *old_file, const char *new_file)
{
	status_t rename_status = rename(new_file, old_file);
	int expression = (SUCCESS != rename_status); 
	return (RetStatus(expression, RENAME_ERROR, SUCCESS));
}

