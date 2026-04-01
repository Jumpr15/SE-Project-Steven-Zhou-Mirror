from engine import create_db_and_tables, ret_session

from User.UserDAO import insert_user, delete_user, update_user, get_user, user_exists

from Conversation.ConversationDAO import insert_conversation

create_db_and_tables()

session = ret_session()


user = insert_user("zheng", "123", session)
convo = insert_conversation("zheng", "my chronicles", session)


     
     