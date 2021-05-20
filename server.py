from aiogram import Bot, Dispatcher, executor, types

import logging

import users
import categories
import user_categories
import timetable
import exceptions

API_TOKEN = '1888208922:AAEKSrE94At7dm_CZrjJ3eBDpyNKrdy3av8'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение"""
    await message.answer(
        "Привет, это наш TimeSheets бот!\n\n"
        "Вы можете ознакомиться с идеей бота по ссылке:\n\n"
        "https://vc.ru/life/143273-12-mesyacev-vedu-pochasovoy-uchet-svoih-del-s-pomoshchyu-timesheets-rasskazyvayu-k"
        "-chemu-eto-v-itoge-privelo\n\n"
        "Напишите /go, если хотите начать"
    )


@dp.message_handler(commands=['go'])
async def start_using(message: types.Message):
    """Отправляет приветственное сообщение"""
    telegram_id = message.from_user.id
    if not users.check_user_in_users_db(telegram_id):
        users.add_user_to_db(telegram_id)
        await message.answer(
            "Отлично!\n"
            "Теперь у Вас есть еще одна возможность контролировать время!\n"
            "Для ознакомления с документацией напишите /help"
        )

    else:
        await message.answer(
            "Вы уже используете наш бот!\n"
            "Для ознакомления с документацией напишите /help"
        )


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer(
        "Чтобы добавить категорию, напишите /add_category, а затем перечислите их через запятую\n"
        "Например:\n"
        "/add_category Еда, Быт, Бот, Проект\n"
        "Посмторесть свои категории можно по команде /categories\n\n"
        "Чтобы добавить временной слот с категорией, напишите сообщение в формате:\n"
        "Категория, ЧЧ:ММ-ЧЧ:ММ\n"
        "Например:\n"
        "Еда, 13:30-14:00\n\n"
        "Получить статистику за день: /today\n"
        "Получить статистику за неделю: /week"

    )


@dp.message_handler(lambda message: message.text.startswith('/add_category'))
async def add_category(message: types.Message):
    person_categories = message.text[14:]
    categories.add_category(person_categories)
    user_categories.add_user_categories(message.from_user.id, person_categories)
    answer_message = "Добавлены категории времяпрепровождения:\n\n* " + \
                     ("\n* ".join([c for c in person_categories.split(', ')]))
    await message.answer(answer_message)


@dp.message_handler(commands=['categories'])
async def get_categories(message: types.Message):
    person_categories = list(user_categories.get_user_categories(message.from_user.id))
    print(person_categories)
    answer_message = "Ваши категории времяпрепровождения:\n\n* " + \
                     ("\n* ".join(c[0] for c in person_categories))
    await message.answer(answer_message)


@dp.message_handler(lambda message: message.text.startswith('/del'))
async def del_user_category(message: types.Message):
    del_category = message.text[5:]
    print(del_category)
    row_id = user_categories.get_id_user_categories(telegram_id=message.from_user.id,
                                                    category=del_category.lower())
    print(row_id)
    user_categories.del_usres_category(row_id=row_id)


@dp.message_handler(commands=['today'])
async def get_today_statistics(message: types.Message):
    answer_message = timetable.get_today_statistics(message.from_user.id)
    doc = open(f'user_plots/{message.from_user.id}_pie_plot.png', 'rb')
    await bot.send_photo(message.from_user.id, doc)
    # return timetable.del_user_plot(message.from_user.id)


@dp.message_handler()
async def add_time_note(message: types.message):
    try:
        time_note = timetable.add_time_note(message.from_user.id, message.text)
    except (exceptions.NotCorrectMessage, exceptions.NotYourCategory) as e:
        await message.answer(str(e))
        return
    answer_message = (
        f"Добавлена категория {time_note.category} в промежутке {time_note.start_time[11:]}:{time_note.end_time[11:]}"
    )

    await message.answer(answer_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
