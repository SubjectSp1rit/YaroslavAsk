import pymysql
from config import *

# подключение к бд
try:
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Подключение успешно.")

    try:
        with connection.cursor() as cursor:
            query = "SELECT "
            cursor.execute(query)
            print("Запрос выполнен успешно")
            # cursor.execute(ЗАПРОС)
    finally:
        connection.close()
except Exception as ex:
    print(f"Неудачное подключение: {ex}")
