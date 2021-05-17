from aiogram import Bot, Dispatcher, executor, types
import users

API_TOKEN = '1888208922:AAEKSrE94At7dm_CZrjJ3eBDpyNKrdy3av8'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение"""
    await message.answer(
        "Привет, это наш TimeSheets бот!\n"
        "Вы можете ознакомиться с идеей бота по ссылке:\n"
        "https://vc.ru/life/143273-12-mesyacev-vedu-pochasovoy-uchet-svoih-del-s-pomoshchyu-timesheets-rasskazyvayu-k"
        "-chemu-eto-v-itoge-privelo\n"
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
            "Чтобы добавить свои категории, напищшите команду /"
        )

    else:
        await message.answer(
            "Вы уже используете наш бот!"
        )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
