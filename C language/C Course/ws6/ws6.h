/* Reviewed by ... */
#ifndef __WS6_H__
#define __WS6_H__

typedef enum
{
	SUCCESS,
	ERROR,
	EXIT_BY_USER,
	OPEN_ERROR,
	CLOSE_ERROR,
	WRITE_ERROR,
	READ_ERROR,
	DELETE_ERROR,
	CREATE_FILE_ERROR,
	RENAME_ERROR
} status_t;
typedef status_t (*act_ptr_t)(const char *filename, char *user_input);
typedef int (*comp_ptr_t)(const char *s, const char *cmd);

typedef struct decision
{
	const char *command;
	comp_ptr_t comparison;
	act_ptr_t operation;
} handlers_t;

status_t ChainOfResponsibility(const char *filename, char *user_input);
status_t AddToBegining(const char *file_name, char *write_string);
status_t CountStrFile(const char *file_name, char *user_input);
status_t AddToEndFile(const char *file_name, char *write_string);
status_t RemoveFile(const char *filename, char *user_input);
status_t Exit(const char *filename, char *user_input);
int PhaseTwo(const char *filename);
int DefaultValue();
int CompareFirstChar(const char *input_string, const char *command);

#endif

