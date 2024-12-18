import psycopg2


with psycopg2.connect(
    database="netology_db", user="postgres", password="2709200227092002"
) as conn:
    with conn.cursor() as cur:
        # Функция, удаляющая таблицу
        def del_table(cur, name):
            cur.execute(
                f"""
                DROP TABLE {name};
                """
            )
            conn.commit()

        # Функция, создающая структуру БД (таблицы)
        def create_table(cur, name: str):
            cur.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {name}(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(60) UNIQUE
                );
                """
            )
            conn.commit()

        # Функция, позволяющая добавлять в структуру БД столбец
        def add_column(cur, name_table, new_column_name, data_type, constraint=None):
            cur.execute(
                f"""
                ALTER TABLE {name_table} ADD COLUMN {new_column_name} {data_type} {constraint};
            """
            )
            conn.commit()

        # Функция, позволяющая создать связи таблиц
        def add_table_relationships(cur, name_tadle_1, name_table_2, data_type):
            cur.execute(
                f"""
                {name_tadle_1} {data_type} REFERENCES {name_table_2};
            """
            )
            conn.commit()

        # Функция, позволяющая добавить нового клиента
        def add_client(cur, name_table, first_name, second_name, email, phone_number):
            cur.execute(
                f"""
                INSERT INTO {name_table}(first_name, second_name, email, phone_number) VALUES
                    ('{first_name}', '{second_name}', '{email}', '{phone_number}')
                    RETURNING first_name, second_name, email, phone_number;
                """
            )
            print(cur.fetchone())

        # Функция, позволяющая добавить телефон для существующего клиента
        def add_phone_numbers(cur, name_table, phone_num):
            cur.execute(
                f"""
                INSERT INTO {name_table}(phone_num) VALUES
                ('{phone_num}')
                RETURNING phone_num;
            """
            )
            print(cur.fetchone())

        # Функция, позволяющая изменить данные о клиенте
        def change_info_client(cur, name_table, name_column, update_name_column, id):
            cur.execute(
                f"""
                 UPDATE {name_table} SET {name_column}=%s WHERE id=%s;
        """,
                (f"{update_name_column}", id),
            )
            print(cur.fetchall())

        # Функция, позволяющая удалить телефон для существующего клиента
        def del_clients_phonr_number(cur, name_table, phone_number_id):
            cur.execute(
                f"""
                DELETE FROM {name_table} WHERE id=%s;
            """,
                ({phone_number_id},),
            )
            print(cur.fetchall())

        # Функция, позволяющая удалить существующего клиента
        def del_client(cur, name_table, id_client):
            cur.execute(
                f"""
                DELETE FROM {name_table} WHERE id=%s;
            """,
                ({id_client},),
            )
            print(cur.fetchall())

        # Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону
        def find_client(
            cur,
            client,
            name_table,
            first_name=None,
            second_name=None,
            email=None,
            phone_number=None,
        ):
            cur.execute(
                f"""
                SELECT {client} FROM {name_table} 
                WHERE first_name=%s or second_name=%s or email=%s or phone_number=%s;
            """,
                ({first_name}, {second_name}, {email}, {phone_number}),
            )

        def returning_all_info(name_table):
            cur.execute(
                f"""
                SELECT * FROM {name_table};
            """
            )
            print(cur.fetchall())

        # table_client = del_table(cur, 'client')
        # table_client = del_table(cur, 'phone_number')
