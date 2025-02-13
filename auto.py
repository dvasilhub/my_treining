# Необходимо создать 2 класса: Vehicle и Sedan,
# где Vehicle - это любой транспорт, а Sedan(седан) -
# наследник класса Vehicle.

class Vehicle: # Родительский класс, содержащий атрибуты объекта и атрибуты класса
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white'] #атрибут класса
    def __init__(self, owner, __model, __color, __engine_power): #атрибуты объекта
        self.owner: str = owner
        self.__model: str = __model
        self.__engine_power: int = __engine_power
        self.__color: str = __color

    # Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
    def get_model(self):
        return f"Модель: {self.__model}"

    # Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
    def horse_power(self):
        return f'Мощность двигателя: {self.__engine_power}'

    # Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
    def get_color(self):
        return f'Цвет: {self.__color}'

    # Метод print_info - распечатывает результаты методов
    def print_info(self):
        print(self.get_model())
        print(self.horse_power())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

        # Метод set_color - принимает аргумент new_color(str)
    def set_color(self, new_color: str):
        # если он есть в списке __COLOR_VARIANTS, меняет цвет __color на new_color
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        # в противном случае выводит на экран надпись
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()