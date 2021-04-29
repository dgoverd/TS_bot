# TODO Реализовать работу с таблицей user_category.
#  1. Добавление данной категории для данного пользоателя
#  2. Возможность извлечения категорий для даннного пользователя

import db


def _add_user_categories(telegram_id: int, category_names: str):
    telegram_id = int(telegram_id)
    category_names = category_names.split(', ')
    for category in category_names:
        db.insert(
            table="user_categories",
            column_values={'user_id': telegram_id,
                           'category_id': category}
        )


def get_user_categories(telegram_id: int):
    telegram_id = int(telegram_id)
    cursor = db.get_cursor()
    cursor.execute("select category_id from user_categories where user_id=?", (telegram_id,))
    user_categories = cursor.fetchall()
    print(user_categories)
