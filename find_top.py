def find_top_20(candidates: list) -> list:
    """
    Функция принимает на вход список сводной информации по абитуриентам (candidates)
    и возвращает список с именами 20 человек,
    набравших наибольшее СУММАРНОЕ количество баллов (с учетом extra баллов),
    которые станут студентами университета.
    """
    candidate_scores = []
    top_20 = []
    for candidate in candidates:
        scores_sum = candidate["scores"]["math"] \
                     + candidate["scores"]["russian_language"] \
                     + candidate["scores"]["computer_science"] \
                     + candidate["extra_scores"]
        candidate_scores.append((candidate["name"], scores_sum))

    candidate_scores.sort(key=lambda i: i[1], reverse=True)

    for candidate_name, candidate_score in candidate_scores:
        #        top_20.append((len(top_20) + 1, candidate_name, candidate_score))       #строчка для проверки
        top_20.append(candidate_name)
        if len(top_20) >= 20:
            break

    return top_20


candidates = [
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Slava", "scores": {"math": 40, "russian_language": 52, "computer_science": 48}, "extra_scores": 0},
    {"name": "Nadya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Fedor", "scores": {"math": 92, "russian_language": 31, "computer_science": 34}, "extra_scores": 1},
    {"name": "Roman", "scores": {"math": 58, "russian_language": 62, "computer_science": 24}, "extra_scores": 2},
    {"name": "Alex", "scores": {"math": 80, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Ilya", "scores": {"math": 21, "russian_language": 33, "computer_science": 34}, "extra_scores": 4},
    {"name": "Nata", "scores": {"math": 60, "russian_language": 62, "computer_science": 24}, "extra_scores": 0},
    {"name": "Igor", "scores": {"math": 80, "russian_language": 80, "computer_science": 42}, "extra_scores": 4},
    {"name": "Valya", "scores": {"math": 21, "russian_language": 33, "computer_science": 37}, "extra_scores": 4},
    {"name": "Kostya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Nefedya", "scores": {"math": 36, "russian_language": 85, "computer_science": 52}, "extra_scores": 2},
    {"name": "Sveta", "scores": {"math": 92, "russian_language": 85, "computer_science": 34}, "extra_scores": 1},
    {"name": "Kpss", "scores": {"math": 40, "russian_language": 20, "computer_science": 30}, "extra_scores": 0},
    {"name": "Katya", "scores": {"math": 15, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Fedor_2", "scores": {"math": 92, "russian_language": 40, "computer_science": 34}, "extra_scores": 2},
    {"name": "Roman_3", "scores": {"math": 61, "russian_language": 62, "computer_science": 24}, "extra_scores": 2},
    {"name": "Arny", "scores": {"math": 80, "russian_language": 85, "computer_science": 58}, "extra_scores": 3},
    {"name": "Mary", "scores": {"math": 46, "russian_language": 33, "computer_science": 34}, "extra_scores": 4},
    {"name": "Natalya", "scores": {"math": 60, "russian_language": 70, "computer_science": 24}, "extra_scores": 1},
    {"name": "Artem", "scores": {"math": 80, "russian_language": 80, "computer_science": 65}, "extra_scores": 5},
    {"name": "Dima", "scores": {"math": 89, "russian_language": 33, "computer_science": 37}, "extra_scores": 3}
]

if __name__ == '__main__':
    result = find_top_20(candidates)
    print(result)
