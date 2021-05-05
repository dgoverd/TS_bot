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
