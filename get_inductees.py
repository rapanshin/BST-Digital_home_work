def get_inductees(names: list, birthday_years: list, genders: list) -> list:
    """
    Функция get_inductees принимает 3 списка одинаковой длины.
    В первом списке (names) — имена студентов, позволяющие их точно идентифицировать.
    Во втором (birthday_years) — год рождения.
    В третьем (genders) — пол студента.Частично они отсутствуют ввиду испорченного листа бумаги.
    Функция возвращает список с именами студентов мужского пола, которые достигли или могут достигнуть 18 лет в 2021 году,
    но при этом не старше 30 лет.
    Cтуденты, по которым невозможно точно установить - попадают они в список или нет (из-за порчи данных), должны быть выведены отдельно.
    """


names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]



if __name__ == '__main__':
    result = get_inductees(names, birthday_years, genders)
    print(result)
