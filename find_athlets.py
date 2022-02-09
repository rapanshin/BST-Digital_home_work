def find_athlets(know_english: list, sportsmen: list, more_than_20_years: list) -> list:
    """
    Функция find_athlets принимает 3 списка с именами студентов.
    В первом списке (know_english) — список тех, кто хорошо владеет английским языком.
    Второй (sportsmen) — содержит имена тех, кто увлекается спортом.
    Ну и третий (more_than_20_years) — предоставляет информацию о тех, кто старше 20 лет.
    Функция возвращает список имен студентов, которые подходят под все три критерия. Пример входных данных приведен ниже.
    """
    atlets = list(set(know_english) & set(sportsmen) & set(more_than_20_years))
    return atlets

know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]

if __name__ == '__main__':
    result = find_athlets(know_english, sportsmen, more_than_20_years)
    print(result)
