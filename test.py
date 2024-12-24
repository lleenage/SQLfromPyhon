import psycopg2


# Функция, позволяющая удалять структуру БД
def del_table(name: str):
    with psycopg2.connect(
        database="netology_db", user="postgres", password="2709200227092002"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DROP TABLE {};
                """.format(
                    name
                )
            )
    conn.close()

    # Функция, позволяющая создавать структуру БД


def create_table(name: str):
    with psycopg2.connect(
        database="netology_db", user="postgres", password="2709200227092002"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS {}(
                    id SERIAL PRIMARY KEY
                );
                """.format(
                    name
                )
            )
    conn.close()

    # Функция, позволяющая удалять из структуры БД столбец


def del_column(name_table, column_name):
    with psycopg2.connect(
        database="netology_db", user="postgres", password="2709200227092002"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                ALTER TABLE {} DROP COLUMN {};
            """.format(
                    name_table, column_name
                )
            )
    conn.close()

    # Функция, позволяющая добавлять в структуру БД столбец


def add_column(name_table, new_column_name, data_type, constraint):
    with psycopg2.connect(
        database="netology_db", user="postgres", password="2709200227092002"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                ALTER TABLE {} ADD COLUMN {} {} {};
            """.format(
                    name_table, new_column_name, data_type, constraint
                )
            )
    conn.close()

    # Функция, позволяющая создать связи таблиц


def add_table_relationships(name_table_1, tadle_id, name_table_2):
    with psycopg2.connect(
        database="netology_db", user="postgres", password="2709200227092002"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                ALTER TABLE {} ADD COLUMN
                {} REFERENCES {}(id);
                """.format(
                    name_table_1, tadle_id, name_table_2
                )
            )
    conn.close()

    # Функция, позволяющая добавить нового клиента


def add_client(name_table, first_name, second_name, email):
    with psycopg2.connect(
        database="netology_db", user="postgres", password="2709200227092002"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO {}(first_name, second_name, email) VALUES
                    ('{}', '{}', '{}')
                    RETURNING first_name, second_name, email;
                """.format(
                    name_table, first_name, second_name, email
                )
            )
            print(cur.fetchone())
    conn.close()

    # Функция, позволяющая добавить телефон для существующего клиента


def add_phone_numbers(number, client_id):
    with psycopg2.connect(
        database="netology_db", user="postgres", password="2709200227092002"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO phone_number(number, client_id) VALUES
                ('{}', '{}')
                RETURNING client_id, number;
            """.format(
                    number, client_id
                )
            )
            print(cur.fetchone())
    conn.close()

    # Функция, позволяющая изменить данные о клиенте


def change_info_client(name_column, new_date, id):
    with psycopg2.connect(
        database="netology_db", user="postgres", password="2709200227092002"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE client SET {} = '{}' WHERE id={};
            """.format(
                    name_column, new_date, id
                )
            )
    conn.close()

    # Функция, позволяющая удалить телефон для существующего клиента


def del_clients_phone_number(phone_number_id):
    with psycopg2.connect(
        database="netology_db", user="postgres", password="2709200227092002"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM phone_number WHERE id={};
            """.format(
                    phone_number_id
                )
            )
    conn.close()

    # Функция, позволяющая удалить существующего клиента


def del_client(id_client):
    with psycopg2.connect(
        database="netology_db", user="postgres", password="2709200227092002"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM client WHERE id={};
                """.format(
                    id_client
                )
            )
    conn.close()

    # Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону


def find_client_by_info(first_name="%", second_name="%", email="%"):
    with psycopg2.connect(
        database="netology_db", user="postgres", password="2709200227092002"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM client 
                WHERE first_name='{}' or second_name='{}' or email='{}';
                """.format(
                    first_name, second_name, email
                )
            )
            print('Найден клиент c персональным id и личными данными:', cur.fetchall()[0])
    conn.close()


def find_client_by_phone_number(phone_number):
    with psycopg2.connect(
        database="netology_db", user="postgres", password="2709200227092002"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM phone_number 
                WHERE number='{}';
                """.format(
                    phone_number
                )
            )
            print('Найден клиент с личным номером телефона и персональным id:', cur.fetchall()[0][1:])
    conn.close()


def returning_all_info(name_table):
    with psycopg2.connect(
        database="netology_db", user="postgres", password="2709200227092002"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM {};
                """.format(
                    name_table
                )
            )
            print(cur.fetchall())
    conn.close()


# del_table('phone_number') #удаляем таблицу phone_number
# del_table("client")  #удаляем таблицу client

# create_table('client')  #создаем таблицу client
# create_table("phone_number")  # создаем таблицу phone_number

# del_column('client', 'first_name')  #удаляем столбец first_name из таблицы client
# del_column('client', 'second_name')  #удаляем столбец second_name из таблицы client
# del_column("client", "email")  # удаляем столбец email из таблицы client

# add_column('client', 'first_name', 'VARCHAR(40)', 'NOT NULL')  #добавляем с таблицу client столбец first_name
# add_column('client', 'second_name', 'VARCHAR(40)', 'NOT NULL')  #добавляем с таблицу client столбец second_name
# add_column('client', 'email', 'VARCHAR(60)', 'NOT NULL')  #добавляем с таблицу client столбец email

# add_column("phone_number", "number", "INTEGER", "UNIQUE")  #добавляем с таблицу phone_number столбец number
# add_table_relationships('phone_number', 'client_id INTEGER', 'client')  #создаем отношение таблицы phone_number_id к clien


# add_client("client", "Джон", "Винчестер", "jonv@gmail.com")  #добавили клиента
# add_client("client", "Сэм", "Винчестер", "semv@gmail.com")  #добавили клиента
# add_client("client", "Дин", "Винчестер", "deanv@gmail.com")  #добавили клиента

# add_phone_numbers('7573952', '2') #добавляем номер телефона для существующего клиента
# add_phone_numbers('7573952', '3')
# add_phone_numbers('567489', '3')
# add_phone_numbers("3857629", "3")
# add_phone_numbers('9876543', '3')

# change_info_client('email', 'restandpeacejohn@gmail.com', '1') #изменяем данные столбца email
# change_info_client('first_name', 'пиьдвлтдв', '1') #изменяем данные столбца first_name
# change_info_client('second_name', 'Выотпоытп', '1') #изменяем данные столбца second_name
# change_info_client('second_name', 'Winchester', 2)  #изменяем данные столбца second_name

# find_client_by_info('%', '%', 'deanv@gmail.com')  #находим клиента по email
# find_client_by_phone_number("3857629")  #находим клиента по номеру телефона


# del_clients_phone_number(1)  #удаляем номер телефона
# del_client(1)  #удаляем клиента


returning_all_info('client')  #выводим всю информацию из таблицы client
returning_all_info('phone_number')  #выводим всю информацию из таблицы phone_number