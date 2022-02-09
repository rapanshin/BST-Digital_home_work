import xlsxwriter
import os


def make_report_about_top3(students_avg_scores: dict) -> str:
    """
    Функция make_report_about_top3 принимает словарь (students_avg_scores),
    в котором ключами являются имена студентов, а значениями — средний балл за всю учебу.
    Функция находит ТОП-3 студентов, чей средний балл выше, чем у других.
    Функция возвращает ссылку на эксель-файл, в котором упомянуты 3 студента и который потом будет передан в бухгалтерию.
    Сам файл необходимо создать внутри функции.
    Важно сохранить совместимость с Excel, чтобы Ольга Петровна смогла без проблем получить всю нужную информацию.
    Пример входных данных приведен ниже
    """

    top_3_students = {}
    students_avg_scores_arr = []
    i = 1
    """
    Нашел два варианта решения.
    В первом находим максимальное значение в словаре, добавляем его в top_3_students и удаляем ключ из словаря.
    """
    # while i <= 3:
    #    max_score = max(students_avg_scores.values())
    #    for k, v in students_avg_scores.items():
    #        if v == max_score:
    #            top_3_students[i] = (k, v)
    #            students_avg_scores.pop(k)
    #            break
    #    i += 1
    """
    Во втором переводим словарь в список кортежей, сортируем его и берем первые три значения в top_3_students
    """
    for k, v in students_avg_scores.items():
        students_avg_scores_arr.append((k, v))

    students_avg_scores_arr.sort(key=lambda i: i[1], reverse=True)

    for students_name, students_score in students_avg_scores_arr:
        top_3_students[i] = (students_name, students_score)
        i += 1
        if i > 3:
            break

    """
    Обычно для выгрузки табличных данных используют CSV файлы. 
    В таком случае достаточно стандартных модулей.
    Но поскольку из задания не ясно, умеет ли Ольга Петровна открывать CSV фалы в EXEL 
    устанавливаем и ипортируем xlsxwriter.
    """
    workbook = xlsxwriter.Workbook("top_3_students.xlsx")
    worksheet = workbook.add_worksheet()

    worksheet.write(0, 0, "Номер")
    worksheet.write(0, 1, "Имя")
    worksheet.write(0, 2, "Балл")

    row = 1
    col = 0
    for number in top_3_students:
        worksheet.write(row, col, number)
        worksheet.write(row, col + 1, top_3_students[number][0])
        worksheet.write(row, col + 2, top_3_students[number][1])
        row += 1

    workbook.close()

    return f"{os.getcwd()}top_3_students.xlsx"


students_avg_scores = {
    'Max': 4.964,
    'Eric': 4.962,
    'Peter': 4.923,
    'Mark': 4.957,
    'Julie': 4.95,
    'Jimmy': 4.973,
    'Felix': 4.937,
    'Vasya': 4.911,
    'Don': 4.936,
    'Zoi': 4.937
}

if __name__ == '__main__':
    result = make_report_about_top3(students_avg_scores)
    print(result)
