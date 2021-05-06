# TODO Реализовать работу с таблицей user_category.
#  1. Добавление данной категории для данного пользоателя
#  2. Возможность извлечения категорий для даннного пользователя

import db


def add_user_categories(telegram_id: int, category_names: str):
    telegram_id = int(telegram_id)
    category_names = category_names.split(', ')
    for category in category_names:
        if _check_user_category_in_users_categories_db(telegram_id, category):
            db.insert(
                table="user_categories",
                column_values={'user_id': telegram_id,
                               'category_id': category.lower()}
            )


def _check_user_category_in_users_categories_db(telegram_id: int, category: str) -> bool:
    cursor = db.get_cursor()
    cursor.execute("SELECT count(*) FROM user_categories WHERE (user_id, category_id) = (?, ?)",
                   (telegram_id, category.lower()))
    exist = cursor.fetchone()[0]
    print(exist)
    if exist == 0:
        return True
    else:
        return False


def check_user_category_in_users_categories_db(telegram_id: int, category: str) -> bool:
    cursor = db.get_cursor()
    cursor.execute("SELECT count(*) FROM user_categories WHERE (user_id, category_id) = (?, ?)",
                   (telegram_id, category.lower()))
    exist = cursor.fetchone()[0]
    print(exist)
    if exist == 1:
        return True
    else:
        return False


def get_user_categories(telegram_id: int):
    telegram_id = int(telegram_id)
    cursor = db.get_cursor()
    cursor.execute("select category_id from user_categories where user_id=?", (telegram_id,))
    user_categories = cursor.fetchall()
    print(user_categories)


def get_id_user_categories(telegram_id: int, category: str):
    telegram_id = int(telegram_id)
    cursor = db.get_cursor()
    cursor.execute("select id from user_categories where (user_id, category_id)=(?, ?)",
                   (telegram_id, category.lower()))
    user_categories = cursor.fetchone()[0]
    print(user_categories)
