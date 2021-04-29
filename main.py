import db
import users
import categories
import user_categories

if __name__ == "__main__":
    print("a")
    db.check_init_db()
    db.insert(table='users', column_values={'telegram_id': '1'})
    db.insert(table='categories', column_values={'category_name': 'Food'})
    # db.delete(table='categories', codename='1')
    db.insert(table='user_categories', column_values={'user_id': '1', 'category_id': 'Food'})
    db.insert(table='categories', column_values={'category_name': 'Bot'})
    db.insert(table='users', column_values={'telegram_id': '2'})
    db.insert(table='user_categories', column_values={'user_id': '2', 'category_id': 'Food'})
    db.insert(table='user_categories', column_values={'user_id': '1', 'category_id': 'Bot'})
    users._add_user_to_db(5)
    categories.add_category('Food, Sport, Chill')
    user_categories._add_user_categories(5, 'Food')
    user_categories.get_user_categories(5)
