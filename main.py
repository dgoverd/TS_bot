import db
import users
import categories
import user_categories

if __name__ == "__main__":
    db.check_init_db()
    users.add_user_to_db(1)
    users.add_user_to_db(2)
    users.add_user_to_db(3)
    categories.add_category('Food, Sport, Chill')
    user_categories.add_user_categories(2, 'Chill, Sport')
    user_categories.get_user_categories(3)
