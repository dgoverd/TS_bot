import db

if __name__ == "__main__":
    print("a")
    db.check_init_db()
    db.insert('users', {'codename': '2', 'telegram_id': '1234512345'})
    db.insert('categories', {'codename': '1'})
