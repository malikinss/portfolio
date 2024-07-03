'''
TODO:
        Below is a program that should convert the specs dictionary into a
        JSON string and output it with three-space indents, without replacing
        Cyrillic characters with their codes.

        There is an error in the program, so it outputs:
        {"\u041c\u043e\u0434\u0435\u043b\u044c": "AMD Ryzen 5 5600G",
        "\u0413\u043e\u0434 \u0440\u0435\u043b\u0438\u0437\u0430": 2021,
        "\u0421\u043e\u043a\u0435\u0442": "AM4",
        "\u0422\u0435\u0445\u043f\u0440\u043e\u0446\u0435\u0441\u0441": "7 \u043d\u043c",
        "\u042f\u0434\u0440\u043e": "Cezanne",
        "\u041e\u0431\u044a\u0435\u043c \u043a\u044d\u0448\u0430 L2": "3 \u041c\u0411",
        "\u041e\u0431\u044a\u0435\u043c \u043a\u044d\u0448\u0430 L3": "16 \u041c\u0411",
        "\u0411\u0430\u0437\u043e\u0432\u0430\u044f \u0447\u0430\u0441\u0442\u043e\u0442\u0430 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u0430": "3900 \u041c\u0413\u0446"}

        Find and fix it so that the program converts the specs dictionary to a
        JSON string and outputs it with three-space indents, without replacing
        Cyrillic characters with their codes.

NOTE:
        The initial part of the response looks like this:
            {
                "Модель": "AMD Ryzen 5 5600G",
                "Год релиза": 2021,
                ...
'''
import json
from typing import Dict


specs: Dict = {
         'Модель': 'AMD Ryzen 5 5600G',
         'Год релиза': 2021,
         'Сокет': 'AM4',
         'Техпроцесс': '7 нм',
         'Ядро': 'Cezanne',
         'Объем кэша L2': '3 МБ',
         'Объем кэша L3': '16 МБ',
         'Базовая частота': '3900 МГц'
        }

specs_json: str = json.dumps(specs, indent='   ', ensure_ascii=False)
print(specs_json)
