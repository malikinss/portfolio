'''
TODO:
        News of dubious content began to appear in the chats
        of one well-known messenger.
        It turned out that a certain youth club decided to play a joke,
        spreading all sorts of nonsense.
        However, such hooliganism bothers gullible people, especially
        those of retirement age, so a group of
        independent programmers decided to develop a bot that could
        assess the degree of reliability of the news, as well as
        classify it into any category.

        Write a program that displays all news in a given category,
        ranking them in ascending order of credibility.

        Input format:
            An arbitrary number of lines are provided as input to the
            program; each line, except the last one, contains the news,
            the category to which it belongs, and its reliability in the
            following format:
                <news> / <category> / <credibility>
            The last line contains a single category.

        Output format:
            The program should display all news that belong to the
            entered category.
            News should be arranged in order of increasing degrees of
            reliability, and if the degrees of reliability coincide, in
            the lexicographical order of the news themselves.
'''
import sys
from collections import defaultdict
from typing import List, Tuple, Dict
from dataclasses import dataclass


@dataclass
class NewsRecord:
    title: str
    category: str
    credibility: float


def read_input() -> List[str]:
    """Reads input from stdin and returns a list of stripped lines."""
    return [line.strip() for line in sys.stdin.readlines()]


def filter_news_by_category(news: List[NewsRecord], category: str) -> List[NewsRecord]:
    """Filters the news records by the specified category."""
    return [record for record in news if record.category == category]


def print_sorted_news(news: Dict[float, List[str]]) -> None:
    """
    Prints the news sorted by credibility and lexicographically within
    the same credibility.
    """
    for rate, titles in news.items():
        for title in titles:
            print(title)


def extract_news_and_category() -> Tuple[List[str], str]:
    """
    Extracts the list of news and the chosen category from the input.
    """
    news = read_input()
    category = news[-1]
    news.pop()
    return news, category


def parse_news_record(record: str) -> NewsRecord:
    """Parses a single news record string into a NewsRecord dataclass."""
    title, category, credibility = record.split('/')
    title = title.strip()
    category = category.strip()
    credibility = float(credibility.strip())

    return NewsRecord(title, category, credibility)


def sort_titles_by_rate(news_dict: Dict[float, List[str]]) -> Dict[float, List[str]]:
    """Sorts titles within each credibility rating lexicographically."""
    for rate in news_dict:
        news_dict[rate] = sorted(news_dict[rate])
    return news_dict


def sort_news_by_credibility(news: List[NewsRecord]) -> Dict[float, List[str]]:
    """
    Sorts news records by credibility and returns a dictionary with
    credibility as keys.
    """
    sorted_news = defaultdict(list)
    for record in news:
        sorted_news[record.credibility].append(record.title)
    sorted_news = sort_titles_by_rate(sorted_news)
    return dict(sorted(sorted_news.items()))


def main() -> None:
    """
    Main function to read, filter, sort, and display news by category
    and credibility.
    """
    news_str, category = extract_news_and_category()
    news_records = [parse_news_record(record) for record in news_str]
    filtered_news = filter_news_by_category(news_records, category)
    sorted_news = sort_news_by_credibility(filtered_news)
    print_sorted_news(sorted_news)


if __name__ == "__main__":
    main()
