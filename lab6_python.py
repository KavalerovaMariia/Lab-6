class Weapons:
    className = 'Weapons'


    def __init__(self, name, count,speed):
        self._name = name
        self._count = count  # _ - не изменить извне
        self._speed = speed
    def get_name(self):  # метод для получение имени
        return self._name

    def set_name(self, n):  # метод для установки имени
        self._name = n

    def info(self):
        print(self._name)
        print(f'Количество патронов в магазине:{self._count}')
        print(f'Скорость стрельбы: {self._speed}')
    def seconds(self):
        print(f'За сколько секунд магазин опустеет: {self._count / (self._speed / 60)}')






# за сколько секунд магазин пустеет
#формула: count/(speed/60)  = seconds
class Assault_rifle(Weapons):
    className = 'Assault_rifle'

    def __init__(self, name,count,speed,distance):
        super().__init__(name,count,speed)
        self._distance = distance

    def info(self):
        super().info()
        print(f'Дальность стрельбы: {self._distance}')

    def speed_distance(self):
        print(f'Соотношение скорострельности к дальности стрельбы: {self._speed / self._distance}')


b = Assault_rifle("Объект класса:" + Assault_rifle.className, 30,600,400)
b.info()
b.speed_distance()
b.seconds()
print('\n')
class Sniper_rifle(Weapons):
    className = 'Sniper_rifle'

    def __init__(self, name,count,speed,distance):
        super().__init__(name,count,speed)
        self._distance = distance

    def info(self):
        super().info()
        print(f'Дальность стрельбы: {self._distance}')

    def speed_distance(self):
        print(f'Соотношение скорострельности к дальности стрельбы: {self._speed / self._distance}')


a = Sniper_rifle("Объект класса:" + Sniper_rifle.className, 30,600,1500)
a.info()
a.speed_distance()
a.seconds()



