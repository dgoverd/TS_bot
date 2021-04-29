import db

if __name__ == "__main__":
    print("a")
    db.check_init_db()
    db.insert(table='users', column_values={'codename': '2', 'telegram_id': '1234512345'})
    db.insert(table='categories', column_values={'codename': '1'})
    db.delete(table='categories', codename='1')
    db.insert(table='categories', column_values={'codename': '1', 'name': 'sleep'})
