# TODO Работа с таблицей категорий, их добавление итп
import db

def add_category(category_names: str):  # вводим желаемые категории списком через запятую: Еда, Бот, Спорт, Быт
    category_names = category_names.split(', ')
    for category in category_names:
        db.insert(
            table='categories',
            column_values={'category_name': category.lower()}
        )


def check_category_in_categories_db(category: str) -> bool:
    cursor = db.get_cursor()
    cursor.execute("SELECT count(*) FROM categories WHERE category_name = ?", (category,))
    exist = cursor.fetchone()
    if exist[0] is None:
        print('False')
        return False
    else:
        print("True")
        return True
