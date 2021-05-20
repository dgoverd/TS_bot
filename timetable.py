# TODO Фунции для добавления, выгрузки и анализа статистики с таблицы timetable
from typing import NamedTuple

import db
import parse_message
import user_categories
import exceptions

import pandas as pd
import os


class TimeNote(NamedTuple):
    """Структура новой записи, добавленной в ДБ"""
    start_time: str
    end_time: str
    category: str


def add_time_note(telegram_id: int, raw_message: str):
    message = parse_message.parse_message(telegram_id, raw_message)
    if user_categories.check_user_category_in_users_categories_db(message.telegram_id,
                                                                  message.category):
        db.insert(table="timetable",
                  column_values={
                      "user_id": message.telegram_id,
                      "category_id": message.category,
                      "start_time": message.start_time,
                      "end_time": message.end_time
                  })

        return TimeNote(
            start_time=message.start_time,
            end_time=message.end_time,
            category=message.category
        )

    else:
        raise exceptions.NotYourCategory(
            f"У Вас нет категории {message.category.upper()}"
        )


def get_today_statistics(telegram_id: int):
    cursor = db.get_cursor()
    cursor.execute(
        """SELECT
                category_id,
                sum(CAST((julianday(end_time) - julianday(start_time)) * 24 * 60 AS integer))
            from
                timetable
            where
                user_id=?
            and
                date(start_time)=date('now', 'localtime')
            group by
                category_id""", (telegram_id,)
    )
    today_stat = cursor.fetchall()

    index_categories = []
    categories_values = []

    for elem in today_stat:
        index_categories.append(elem[0])
        categories_values.append(elem[1])

    df = pd.DataFrame({'Time': categories_values}, index=index_categories)
    plot = df.plot.pie(y='Time', figsize=(5, 5))
    fig = plot.get_figure()
    fig.savefig(f'./user_plots/{telegram_id}_pie_plot.png')
    return today_stat


def del_user_plot(telegram_id: int):
    os.remove(f'./user_plots/{telegram_id}_pie_plot.png')
