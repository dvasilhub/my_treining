class House:
    numberOfFloors = 0
    def __init__(self, name, number_of_floors):
        # Инициализируем атрибуты объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"Количество этажей: {self.numberOfFloors}")

    def go_to(self, new_floor):
        # Проверка на допустимость этажа
        if 0 < new_floor <= self.number_of_floors:
            # Вывод последовательности чисел от 1 до new_floor
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            # Сообщение об ошибке
            print("Такого этажа не существует")

# Пример использования класса
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Домик в туалетеле', 1)

# Вызов метода go_to
h1.go_to(5)  # Вывод: 1, 2, 3, 4, 5
h1.setNewNumberOfFloors(18)
h2.go_to(10)  # Вывод: "Такого этажа не существует"
h2.setNewNumberOfFloors(2)
h2.setNewNumberOfFloors(4)
