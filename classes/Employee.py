import Person
from utilities.email_util import email_checker, format_email, write_email


class Employee(Person):
    def __init__(self, emp_id, name, age, is_manager, money=1000, sleep_mood=6, health_rate=100,
                 email='example@gmail.com', work_mood='happy', salary=15000):
        super().__init__(name, age, money, sleep_mood, health_rate)
        self._id = emp_id
        self._is_manager = is_manager
        self._email = email
        self._work_mood = work_mood
        self._salary = salary

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        print('checker /in emp class/')
        if email_checker(email):
            self._email = email
        else:
            print('invalid email it is set to null ')
            self._email = None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            print(f'salary for {self.name} cannot be less than 1000 so 1000 was set as a property. ')
            self._salary = 0
        else:
            self._salary = salary

    def work(self, hours):
        if hours > 8:
            self._work_mood = 'tired'
        elif hours == 8:
            self._work_mood = 'happy'
        else:
            self._work_mood = 'lazy'

    def send_email(self, to, sub, body, receiver_name):
        if self._email is not None:
            email = format_email(self._email, to, sub, receiver_name, body)
            write_email(email)
        else:
            print(f"cannot send email as the email for {self.name} is not valid ")
