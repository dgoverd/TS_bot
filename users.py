"""Добавление пользователя в БД при согласии на использование бота"""

import db


# class User:
#      """Структура класса пользователь"""
#      telegram_id: int


def add_user_to_db(telegram_id: int):
    """Добавляет пользоветля в БД при старте работы с ботом"""
    telegram_id = int(telegram_id)
    db.insert(
        table='users',
        column_values={'telegram_id': telegram_id}
    )


def check_user_in_users_db(id: int) -> bool:
    cursor = db.get_cursor()
    cursor.execute("SELECT count(*) FROM users WHERE telegram_id = ?", (id,))
    exist = cursor.fetchone()
    print(exist[0])
    if exist[0] == 0:
        print('False')
        return False
    else:
        print("True")
        return True
