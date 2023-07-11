/*
*************************************
* Title : UID function definitions	*
* Author: Sam Malikin				*
* Reviewer: Micha					*
* Date : 05.05.2023					*
*************************************
*/

#include <stdio.h> /* perror(), printf() */
#include <string.h> /* strstr(), strcmp() */
#include <unistd.h> /* getpid() */
#include <ifaddrs.h> /* getifaddrs(), freeifaddrs(), ifaddrs, sockaddr_in */
#include <netdb.h> /* getnameinfo(), gai_strerror(), AF_INET */
#include <assert.h>


#include "uid.h" /* API */

#define IP_SIZE (14)

typedef enum status {SUCCESS, FAIL} status_t;

typedef struct sockaddr sockaddr_t;
typedef struct ifaddrs ifaddrs_t;

static ifaddrs_t *Ifa_Next(ifaddrs_t *node);
static sockaddr_t *Ifa_Addr(ifaddrs_t *node);
static status_t GetIP(char *ip);

static size_t g_counter = 1;

const ilrd_uid_t BadUID = {0};


ilrd_uid_t UIDCreate(void)
{
	ilrd_uid_t new_UID = {0};

	new_UID.counter = g_counter;
	++g_counter;
	
	if ((time_t)-1 == time(&new_UID.timestamp))
	{
		return (BadUID);
	}
    
	new_UID.pid = getpid();
	
	if(SUCCESS != GetIP(new_UID.ip))
	{
		return (BadUID);
	}
	
	return (new_UID);
}


int UIDIsSame(ilrd_uid_t uid1, ilrd_uid_t uid2)
{
	int check_timestamp = (uid1.timestamp == uid2.timestamp);
	int check_counter = (uid1.counter == uid2.counter);
	int check_pid = (uid1.pid == uid2.pid);
	int check_ip = (0 == memcmp(uid1.ip, uid2.ip, IP_SIZE));	
	int result = (check_timestamp && check_counter && check_pid && check_ip);
	
	return (result);
}



static ifaddrs_t *Ifa_Next(ifaddrs_t *node)
{
	assert(NULL != node);

	return (node->ifa_next);
}

static sockaddr_t *Ifa_Addr(ifaddrs_t *node)
{
	assert(NULL != node);

	return (node->ifa_addr);
}


static status_t GetIP(char *ip) 
{
	ifaddrs_t *device_ip = NULL;
	ifaddrs_t *ip_runner = NULL;
	sockaddr_t *ifa_address = NULL;
	
	
	if (getifaddrs(&device_ip))
	{
		return (FAIL);
	}
	
	ip_runner = device_ip;
	
	ifa_address = Ifa_Addr(ip_runner);
	
	while (AF_INET != ifa_address->sa_family || !strcmp(ip_runner->ifa_name, "lo"))
	{
		ifa_address = Ifa_Addr(ip_runner);
		ip_runner = Ifa_Next(ip_runner);
		
		if (NULL == ip_runner)
		{
			return (FAIL);
		}
	}
	
	if (NULL == ifa_address)
	{
		return (FAIL);
	}
	
	memcpy(ip, ifa_address->sa_data, IP_SIZE);
    	
	freeifaddrs(device_ip);
	device_ip = NULL;
	ip_runner = NULL;
	
	return (SUCCESS);
}
