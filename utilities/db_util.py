import mysql.connector
from mysql.connector import Error


connected = False


def _get_db_cursor():
    global connected
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='company_pyx',
                                             user='Ams')
        if connection.is_connected():
            cursor = connection.cursor()
            connected = True
            return connection, cursor
    except Error as e:
        connected = False
        print(f'failed to connect to mysql db, error : {format(e)}')
        return None, None


def _check_connection(connection, cursor):
    if connection is None and cursor is None:
        print('error in connection')
        return False
    else:
        return True


def create_employees_table():
    connection, cursor = _get_db_cursor()
    if not _check_connection(connection, cursor):
        return
    try:
        if connected:
            create_employee_table_query = '''CREATE TABLE IF NOT EXISTS emp ( 
                                                 id int AUTO_INCREMENT primary key,
                                                 name varchar(50),
                                                 age int,
                                                 is_manager int) '''
            cursor.execute(create_employee_table_query)
            connection.commit()
    except Error as e:
        print(f'Failed to create table in MySQL, error : {format(e)}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def delete_employees_table():
    connection, cursor = _get_db_cursor()
    if not _check_connection(connection, cursor):
        return
    try:
        if connected:
            delete_employee_table_query = '''drop table if exists emp '''
            cursor.execute(delete_employee_table_query)
            connection.commit()
    except Error as e:
        print(f'error deleting table Employees, error : {format(e)}')
    finally:
        if connected:
            connection.close()
            cursor.close()


def add_to_employees_table(name, age, is_manager):
    connection, cursor = _get_db_cursor()
    if not _check_connection(connection, cursor):
        return
    try:
        if connected:
            add_to_employees_table_query = f'''
            INSERT INTO company_pyx.emp(name,age,is_manager) VALUES("{name}",{age},{is_manager});
            '''
            cursor.execute(add_to_employees_table_query)
            connection.commit()
    except Error as e:
        print(f'error adding employee, error : {format(e)}')
    finally:
        if connected:
            connection.close()
            cursor.close()
