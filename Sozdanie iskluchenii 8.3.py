
# Создайте 3 класса (2 из которых будут исключениями):

# Классы исключений IncorrectVinNumber и IncorrectCarNumbers,
# объекты которых обладают атрибутом message - сообщение, которое будет выводиться
# при выбрасывании исключения.

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message


# Класс Car должен обладать следующими свойствами:
class Car:
    def __init__(self, model, vin, numbers):
        # Атрибут объекта model - название автомобиля (строка).
        self.model = model

        # Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
        self.__vin = vin

        # Атрибут __numbers - номера автомобиля (строка).
        self.__numbers = numbers

        # Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
        # Возвращает True, если корректный, в других случаях выбрасывает исключение.
        # Уровень доступа private.
        self.__is_valid_vin(self.__vin)

        # Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
        # Возвращает True, если корректный, в других случаях выбрасывает исключение.
        # Уровень доступа private.
        self.__is_valid_numbers(self.__numbers)

    # Работа методов __is_valid_vin и __is_valid_numbers:

    # __is_valid_vin
    def __is_valid_vin(self, vin_number):
        # Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
        # если передано не целое число. (тип данных можно проверить функцией isinstance).
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')

        # Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
        # если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
        elif not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

        # Возвращает True, если исключения не были выброшены.
        return True

    # __is_valid_numbers
    def __is_valid_numbers(self, numbers):
        # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
        # если передана не строка. (тип данных можно проверить функцией isinstance).
        if not isinstance(numbers, str):
            raise IncorrectCarNumber('Некорректный тип данных для номеров')

        # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
        # переданная строка должна состоять ровно из 6 символов.
        elif not (len(numbers) == 6):
            raise IncorrectCarNumber('Неверная длина номера')

        # Возвращает True, если исключения не были выброшены.
        return True


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
