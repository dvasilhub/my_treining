# Простое число — это натуральное число, которое больше единицы и имеет два конкретных делителя: себя и единицу 1
# Дан список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = [] # только простые числа
not_primes = [] # не простые числа

for number in numbers: # проходим по всем числам
    if number == 1: # 1 число не считаем
        continue
    is_prime = True # считаем по что числа простые
    for i in range(2, number): # для перебора чисел от 2 до заданного значения number
        if number % i == 0: # проверям пару чисел
            is_prime = False # непростое число
            break # выходим из под цикла
    if is_prime: # если простое число
        primes.append(number)
    else: # если не простое число
        not_primes.append(number)

print("Простые числа:", primes)
print("Не простые числа:", not_primes)