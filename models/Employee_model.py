from utilities.db_util import create_employees_table, delete_employees_table, add_to_employees_table


class Employee:

    _is_table_created = False

    @classmethod
    def delete_table(cls):
        delete_employees_table()

    @classmethod
    def create_database(cls):
        create_employees_table()

    @classmethod
    def add_employee(cls, name, age, is_manager):
        cls.create_database()
        add_to_employees_table(name, age, is_manager)
