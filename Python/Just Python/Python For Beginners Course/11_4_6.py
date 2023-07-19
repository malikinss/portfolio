""" 
Task: The input to the program is a natural number n, then n lines, 
then the number k — the number of search requests, then k lines — 
search requests. 
Write a program that prints out all the input strings that contain 
all search queries at the same time.
"""

n = int(input())

strings = []
for _ in range(n):
    s = input()
    strings.append(s)
    
k = int(input())

search_queries = []
for _ in range(k):
    search_query = input()
    search_queries.append(search_query)
    
for s in strings:
    for search_query in search_queries:
        if search_query.lower() not in s.lower():
            break
    else:
        print(s)