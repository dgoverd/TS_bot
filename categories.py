# TODO Работа с таблицей категорий, их добавление и

import db


def add_category(category_names: str):  # вводим желаемые категории списком через запятую: Еда, Бот, Спорт, Быт
    category_names = category_names.split(', ')
    for category in category_names:
        db.insert(
            table='categories',
            column_values={'category_name': category}
        )
