#! /usr/bin/python3
import sys

from models.Employee_model import Employee
from colorama import Fore, Style

print('\n\t company pyx, employees model\n\n')

clear_old_data = input(f'''delete previous data {Fore.RED}(Warning this will drop the database table){Style.RESET_ALL}? 
                           y to confirm ,any button for no [no] : ''')
if clear_old_data == 'y':
    Employee.delete_table()
    Employee.create_database()

choice = ''
while choice != 'q':
    choice = input(f'''new employee > type {Fore.GREEN}add{Style.RESET_ALL} to add or {Fore.RED}q to quit{Style.RESET_ALL} [q]: ''')
    if choice == 'add':
        name = input("Enter the name: ")
        age = input("Enter the age: ")
        level = input(f'''enter whether the employee is a normal or manager for normal
                            {Fore.GREEN}nrml{Style.RESET_ALL} and {Fore.GREEN}mngr{Style.RESET_ALL} for manager [nrml]''')
        # if level == 'nrml':
        #     Employee.add_employee(name, age, False)
        # elif level == 'mngr':
        #     Employee.add_employee(name, age, True)
        # else:
        #     print('wrong choice set to non manager')
        #     Employee.add_employee(name, age, False)
        match level:
            case 'nrml':
                Employee.add_employee(name, age, False)
            case 'mngr':
                Employee.add_employee(name, age, False)
            case default:
                print('wrong choice set to non manager')
                Employee.add_employee(name, age, False)
    else:
        sys.exit()
        # if python 3.10 or higher
        # match level:
        #     case 'nrml':
        #         Employee.add_employee(name, age, False)
        #     case 'mngr':
        #         Employee.add_employee(name, age, False)
        #     case default:
        #         print('wrong choice set to non manager')
        #         Employee.add_employee(name, age, False)
