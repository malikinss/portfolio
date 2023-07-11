""" 
Task: Zoom challenged the Flash and offered him a fair fight 
in the form of a race around the magnetar. 
In the event of a loss, this neutron star will charge up and 
destroy the world, so the Flash decided not to risk it for 
no reason, and ask his friend Cisco Ramon whether it makes 
sense to accept the challenge. 
Cisco received data that Zoom's speed is n and Flash's speed is k.
"""
n = int(input())
k = int(input())
if n>k:
    print('NO')
elif k>n:
    print('YES')
else:
    print("Don't know")