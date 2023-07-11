/* reviewed by somebody */
#include <stdio.h> 		/*printf*/
#include <string.h>		/*strcmp*/
#include <stdlib.h>
#include <math.h>

#include "ws9.h"

static void TestCompare(student_grades *original_grades, 
    student_grades *copy_of_grades);

static int FloatCompare(float num1, float num2);

int main()
{	
	char *filename = NULL;
	
	student_grades student1 = {"Sam", "Malikin", {4.5, {4.8, 5, 5, 4.3, 4.75}, {4.3, 4.8, 4, 3.99, 4.72}}};
	student_grades copy_student1;
	SaveRecord(&student1);
	
	MakeFileName(student1.last_name, &filename);
	LoadRecord(&copy_student1, filename);
	TestCompare(&student1, &copy_student1);
	
	free(filename);
	filename = NULL;
	return 0;
}

static int FloatCompare(float num1, float num2)
{
	if (fabs(num1 - num2) < 0.0001) 
	{
		return 0;
	} 
	else 
	{
		return -1;
	}
}


static void TestCompare(student_grades *original_grades, 
    student_grades *copy_of_grades)
{


	int expression1 = FloatCompare(original_grades->their_grades.sports_grade, copy_of_grades->their_grades.sports_grade);
	int expression2 = FloatCompare(original_grades->their_grades.hum_grades.sociology_grade, copy_of_grades->their_grades.hum_grades.sociology_grade);
	int expression3 = FloatCompare(original_grades->their_grades.hum_grades.psychology_grade, copy_of_grades->their_grades.hum_grades.psychology_grade);
	int expression4 = FloatCompare(original_grades->their_grades.hum_grades.literature_grade, copy_of_grades->their_grades.hum_grades.literature_grade);
	int expression5 = FloatCompare(original_grades->their_grades.hum_grades.economics_grade, copy_of_grades->their_grades.hum_grades.economics_grade);
	int expression6 = FloatCompare(original_grades->their_grades.hum_grades.law_stadies_grade, copy_of_grades->their_grades.hum_grades.law_stadies_grade);
	
	int expression7 = FloatCompare(original_grades->their_grades.real_grades.math, copy_of_grades->their_grades.real_grades.math);	
	int expression8 = FloatCompare(original_grades->their_grades.real_grades.phisics, copy_of_grades->their_grades.real_grades.phisics);
	int expression9 = FloatCompare(original_grades->their_grades.real_grades.chemestry, copy_of_grades->their_grades.real_grades.chemestry);
	int expression10 = FloatCompare(original_grades->their_grades.real_grades.geometry, copy_of_grades->their_grades.real_grades.geometry);	
	int expression11 = FloatCompare(original_grades->their_grades.real_grades.statistics, copy_of_grades->their_grades.real_grades.statistics);
	
	
	
    if (0 == strcmp(original_grades->first_name, 
    copy_of_grades->first_name) &&
    0 == strcmp(original_grades->last_name, 
    copy_of_grades->last_name) && !expression1 && !expression2 && !expression3 && !expression4 && !expression5 && !expression6 && !expression7 && !expression8 && !expression9 && !expression10 && !expression11)
    {
        printf("Compare Test Passed\n");
    }
}
