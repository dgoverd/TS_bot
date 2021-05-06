from typing import NamedTuple, Tuple
import re
from datetime import datetime, date

import exceptions
import categories


class Message(NamedTuple):
    """Структура распаршенного сообщения о новом занятии"""
    start_time: str
    end_time: str
    category: str
    telegram_id: int


def parse_message(telegram_id: int, raw_message: str) -> Message:
    category_and_time = _split_message(raw_message)
    print(category_and_time)
    _check_time_mod_30(category_and_time)
    categories.check_category_in_categories_db(category_and_time[0])
    return Message(telegram_id=telegram_id,
                   end_time=category_and_time[2],
                   start_time=category_and_time[1],
                   category=category_and_time[0])


def _split_message(raw_message: str) -> Tuple[str, str, str]:
    split_message = re.match(r"(.*) (\d\d:\d\d)-(\d\d:\d\d)", raw_message)
    if not split_message or not split_message.group(0) \
            or not split_message.group(1) or not split_message.group(2) or not split_message.group(3):
        raise exceptions.NotCorrectMessage(
            "Не могу понять сообщение. Напишите сообщение в формате, "
            "например:\n Еда 18:00-19:30")
    category = split_message.group(1).lower()
    start_time = _add_today_date_to_time(split_message.group(2))
    end_time = _add_today_date_to_time(split_message.group(3))
    return category, start_time, end_time


def _check_time_mod_30(split_message: Tuple[str, str, str]):
    start_time_minutes = datetime.strptime(split_message[1], '%Y-%m-%d %H:%M').minute
    end_time_minutes = datetime.strptime(split_message[2], '%Y-%m-%d %H:%M').minute
    if (start_time_minutes == 0 or start_time_minutes == 30) and (end_time_minutes == 0 or end_time_minutes == 30):
        return
    else:
        raise exceptions.NotCorrectMessage(
            "Введите время в формате ЧЧ:30 или ЧЧ:00,"
            "например:\n 18:30 или 19:00")


def _add_today_date_to_time(time: str) -> str:
    today_data = date.today()
    f = today_data.strftime('%Y-%m-%d')  # вместо datetime сделали str
    data_time = f + " " + time

    return data_time
