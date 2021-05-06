# TODO Фунции для добавления, выгрузки и анализа статистики с таблицы timetable

import db
import parse_message
import user_categories


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
