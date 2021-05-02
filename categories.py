# ФУНКЦИЯ ПРОВЕРЯЕТ, ЧТО ПОСЛЕ КАТЕГОРИИ ЗАПИСАНО ВРЕМЯ

def check_if_time_in_str(piece_of_str_with_time):
    for i in piece_of_str:
        try:
            date_time_obj = datetime.datetime.strptime(i, '%H:%M')
        except ValueError:
            print("После категории записано не время")

    return piece_of_str_with_time


# ФУНКЦИЯ ПРОВЕРЯЕТ, ЧТО ВРЕМЯ КРАТНО 30 МИНУТАМ

def check_if_time_mod_30min:


# ФУНКЦИЯ ПОЛУЧАЕТ ОТ ПОЛЬЗОВАТЕЛЯ СТРОКУ, ПРОВЕРЯЕТ ЕЕ И В СЛУЧАЕМ ЕСЛИ ВСЕ ОК, ВОЗВРАЩАЕТ ЕЕ ЖЕ

def parse_message(raw_message: str):
    regexp_result = re.split(r',', raw_message)  # разделили на части по ЗАПЯТОЙ на категорию и время
    amount_of_parts = len(regexp_result)

    if amount_of_parts == 0:
        raise exceptions.NotCorrectMessage("Введите еще раз данные")

    elif amount_of_parts == 1:
        raise exceptions.NotCorrectMessage("Дополните информацию")

    elif amount_of_parts == 2:
        pass
    # def(проверка что категория существует) если да, то def проверка что 2й это время
    # категорию делаем lower()

    elif amount_of_parts == 3:
        pass
    # def(проверка что категория существует) если да, то def проверка что 2й и 3й это время, если да, т def проверка что время начало < время конец

    elif amount_of_parts > 3:
        raise exceptions.NotCorrectMessage("Проверьте на наличие лишней информации")

    return spisok  # в случае если все введено верно, возвращаем тот же список, что и пришел


# ФУНКЦИЯ ПРЕОБРАЗОВАНИЯ ВРЕМЕНИ ИЗ STR В DATETIME
def convert_time_from_str_to_datetime(piece_of_str_with_time):
    today_data = datetime.date.today()
    f = today_data.strftime('%Y-%m-%d')  # вместо datetime сделали str
    list_of_dates = []
    for time in piece_of_str_with_time:
        time_new = time.replace(" ", "")
        data = f + " " + time_new
        # print(data) # type str
        date_time_obj = datetime.datetime.strptime(data, '%Y-%m-%d %H:%M')  # сделали из str обратно datetime
        list_of_dates.append(date_time_obj)

    return list_of_dates




# ФУНКЦИЯ ПРИНИМАЕТ СПИСОК ОБРАБАТЫВАЕТ, ВОЗВРАЩАЕТ СПИСОК ['КАТЕГОРИЯ, ВРЕМЯ ПО 30 МИНУТ']
def processing_of_list(spisok):
    list_of_one_pair = []  # список 'категория, время'
    list_of_one_pair.apppend(spisok[0])

    time_raw = spisok.pop([0])  # необработанное время
    list_of_pairs_date_category = []  # наша цель список [ [], [], [] ]

    # вызов ФУНКЦИЯ ПРЕОБРАЗОВАНИЯ ВРЕМЕНИ ИЗ STR В DATETIME

    for t in time_raw:
        list_of_one_pair.apppend(
            date_time_obj)  # добавили к категории время, добавили этот список к списку всех вариков, очистили от времени категорию)
        list_of_pairs_date_category.append(list_of_one_pair)
        list_of_one_pair.pop([1])

    return list_of_pairs_date_category




