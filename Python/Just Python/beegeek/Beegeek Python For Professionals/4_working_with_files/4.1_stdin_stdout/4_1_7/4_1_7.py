'''
TODO:   
        News of dubious content began to appear in the chats of one well-known messenger. 
        
        It turned out that a certain youth club decided to play a joke, spreading all sorts of nonsense. 
        
        However, such hooliganism bothers gullible people, especially those of retirement age, so a group of independent programmers decided to develop a bot that could assess the degree of reliability of the news, as well as classify it into any category.
        
        Write a program that displays all news in a given category, ranking them in ascending order of reliability.

        An arbitrary number of lines are provided as input to the program; each line, except the last one, contains the news, the category to which it belongs, and its reliability in the following format:
            <news> / <category> / <credibility>

        The last line contains a single category.

        The program should display all news that belong to the entered category. 
        
        News should be arranged in order of increasing degrees of reliability, and if the degrees of reliability coincide, in the lexicographical order of the news themselves.

'''
import sys

def read_news_from_input():
    return [line.strip() for line in sys.stdin.readlines()]

def sort_news_db(news):
    for category, record in news.items():
        print(record)
        news[category].update(sorted(record, key=record.keys))

    return news  

def get_news_database(news_list):
    news_db = {}
    
    for item in news_list:
        title, category, number = item.split(' / ')
        number = float(number)
        
        if category not in news_db:
            news_db[category] = {}
        
        if number not in news_db[category]:
            news_db[category][number] = []
        
        news_db[category][number].append(title)

    return sort_news_db(news_db)

  

given_data = read_news_from_input()
given_news = given_data[:-1]
given_filter = given_data[-1]

news = get_news_database(given_news)
#print(news)