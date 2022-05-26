class Person:
    def __init__(self, name, age, money=1000, sleep_mood=4, health_rate=100):
        self._name = name
        self._age = age
        self._money = money
        self._sleep_mood = sleep_mood
        self._health_rate = health_rate

    @property
    def _money(self):
        return self._money

    @_money.setter
    def _money(self, money):
        if money < 0:
            print(f'money for {self._name} cannot be less than 0 so 0 was set as a property. ')
            self._money = 0
        else:
            self._money = money

    @property
    def sleep_mood(self):
        return self._sleep_mood

    @sleep_mood.setter
    def sleep_mood(self, sleep_mode):
        if sleep_mode not in [0-7]:
            print('this sleep mood is not valid tired (4) was set')
            self._sleep_mood = 4
            return
        self._sleep_mood = sleep_mode

    @property
    def _health_rate(self):
        return self.__heathRate

    @_health_rate.setter
    def _health_rate(self, heath_rate):
        if heath_rate not in range(0, 100):
            print(f'health rate cannot be out of 0 to 100  so 100 was set for {self._name}')
            self.__heathRate = 100
            return
        self.__heathRate = heath_rate

    def sleep(self, hours):
        if hours > 7:
            self._sleep_mood = 'lazy'
        elif hours == 7:
            self._sleep_mood = 'happy'
        else:
            self._sleep_mood = 'tired'

    def buy(self, items):
        if self._money - items * 10 > 0:
            self._money -= items * 10
            print(f'you {self._name} bought items by {items * 10} $ and he has now {self._money}')
        else:
            print(f'{self._name} do not have enough money')

    def eat(self, meals):
        if meals == 3:
            self.__heathRate = 100
        elif meals == 2:
            self.__heathRate = 75
        else:
            self.__heathRate = 50

    def __str__(self):
        return f'''
         name:{self._name}
         age:{self._age}
         money:{self._money}
         healthRate:{self.__heathRate} 
         sleeping_mood:{self._sleep_mood}'''
