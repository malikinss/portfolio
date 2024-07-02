'''
TODO:
        Complete the code below so that it converts the words dictionary to a
        JSON string, skipping pairs that have invalid keys, and assigns the
        result to the data_json variable.
'''
import json
from typing import Dict

words: Dict = {
    frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
    "travel": "trævl",
    ("hello", "world"): ("həˈləʊ", "wɜːld"),
    "moonlight": "muːn.laɪt",
    "sunshine": "ˈsʌn.ʃaɪn",
    ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
    "adventure": "ədˈventʃər",
    "beautiful": "ˈbjuːtɪfl",
    frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
    "bicycle": "baisikl",
    ("pilot", "fly"): ("pailət", "flai")}

data_json = json.dumps(words, skipkeys=True)
