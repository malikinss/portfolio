import json

with open("4_3_14/tests/right.json", encoding="utf-8") as file_1, open("4_3_14/tests/best_scores.json", encoding="utf-8") as file_2:
    right_f = json.load(file_1)
    your_f = json.load(file_2)
    i = 0
    while i < len(right_f) and (r := right_f[i]) and (y := your_f[i]):
        if r != y:
            print("=" * 50)
            print("Найдено не соответсвие")
            print(f"Ожидаемый результат\n{'-' * 19}")
            print(r)
            print("-" * 19)
            print(f"Твой результат\n{'-' * 14}")
            print(y)
            print("=" * 50)
        i += 1