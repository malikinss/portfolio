/*
*********************************
* Title : UID header file		*
* Author: Sam Malikin			*
* Reviewer: Micha				*
* Date : 05.05.2023				*
*********************************
*/

#ifndef __UID_H_ILRD__
#define __UID_H_ILRD__

#include <sys/types.h> /* pid_t */ 
#include <time.h> /* time_t */

#define IPV4_MAXHOST (14)

typedef struct UID ilrd_uid_t;

extern const ilrd_uid_t BadUID;

struct UID
{
    size_t counter;
    time_t timestamp;
    pid_t pid;
    char ip[IPV4_MAXHOST];
};

ilrd_uid_t UIDCreate(void); /* O(1) */

int UIDIsSame(ilrd_uid_t uid1, ilrd_uid_t uid2); /* O(1) */

#endif  /* __UID_H_ILRD__ */ 

