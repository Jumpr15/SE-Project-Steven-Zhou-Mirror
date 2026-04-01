from engine import create_db_and_tables, ret_session

from User.UserDAO import insert_user, delete_user, update_user, get_user, user_exists

create_db_and_tables()

session = ret_session()


print(user_exists("hljh", session))

     
     