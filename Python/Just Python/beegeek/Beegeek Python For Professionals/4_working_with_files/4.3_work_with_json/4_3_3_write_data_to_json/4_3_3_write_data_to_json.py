'''
TODO:
        You have access to the club1, club2, and club3 dictionaries, which
        contain data about different football clubs.

        Complete the code below so that it concatenates these dictionaries
        into a list and writes the resulting data structure to the data.json
        file, indented by three spaces.

NOTE:
        The dictionaries in the list must be in their original order.

        The initial part of the data.json file looks like this:
            [
                {
                    "name": "FC Byern Munchen",
                    "country": "Germany",
                    ...
                },
                ...
            ]
'''
import json
from typing import Dict, List, Any


def write_data_to_json(data: Any, indent: Any) -> None:
    with open('data.json', 'w', encoding='utf8') as json_file:
        json.dump(data, json_file, indent=indent)


club1: Dict = {"name": "FC Byern Munchen", "country": "Germany",
               "founded": 1900, "trainer": "Julian Nagelsmann",
               "goalkeeper": "M. Neuer", "league_position": 1}

club2: Dict = {"name": "FC Barcelona", "country": "Spain",
               "founded": 1899, "trainer": "Xavier Creus",
               "goalkeeper": "M. Ter Stegen", "league_position": 7}

club3: Dict = {"name": "FC Manchester United", "country": "England",
               "founded": 1878, "trainer": "Michael Carrick",
               "goalkeeper": "D. De Gea", "league_position": 8}

clubs: List[Dict] = [club1, club2, club3]

write_data_to_json(data=clubs, indent='   ')
