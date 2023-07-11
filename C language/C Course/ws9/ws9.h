/* reviewed by somebody */
#ifndef __WS9_H__
#define __WS9_H__

#include <stdio.h> 		/*FILE*/


typedef enum  
{
    SUCCESS, 
    OPEN_ERROR, 
    CLOSE_ERROR, 
    WRITE_ERROR, 
    READ_ERROR,
    MEM_ALLOC_ERROR 
} status_t;

typedef struct
{
    float math;
    float phisics;
    float chemestry;
    float geometry;
    float statistics;
} real_grades;

typedef struct
{
    float sociology_grade;
    float psychology_grade;
    float literature_grade;
    float economics_grade;
    float law_stadies_grade;
} humanistic_grades;


typedef struct
{
    float sports_grade;
    humanistic_grades hum_grades;
    real_grades real_grades;
} grade;


typedef struct 
{
    char first_name[20];
    char last_name[20];
    grade their_grades;
} student_grades;

status_t OpenNCheckFile(FILE **fptr, char *filename, const char *operation);
status_t WriteNCheckFile(FILE **fptr, size_t size, student_grades *grades);
status_t ReadNCheckFile(FILE **fptr, size_t size, student_grades *grades);
status_t CloseNCheckFile(FILE **fptr);

status_t MakeFileName(char *last_name, char **filename);
status_t SaveRecord(student_grades *grades);
status_t LoadRecord(student_grades *grades, char *filename);

#endif /* __WS9_H__ */

