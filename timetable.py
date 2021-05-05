# TODO Фунции для добавления, выгрузки и анализа статистики с таблицы timetable
from typing import List, NamedTuple

import db


class Message(NamedTuple):
    """Структура распаршенного сообщения о новом занятии"""
    time: str
    category: str
    telegram_id: int


def _parse_message(telegram_id: int, raw_message: str) -> List[Message]:
    pass


def add_time_note(raw_message: str):
    for message in _parse_message(raw_message):
        db.insert("timetable", {
            "user_id": message.telegram_id,
            "category_id": message.category,
            "time": message.time
        })

def get_today_statistics() -> str:
    cursor =db.get_cursor()
    cursor.executenamy("select ")