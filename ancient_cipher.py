def get_password(number):
    password = '' # Пароль пока пуст
    for i in range(1, number): # индекс i от 1 до number
        for j in range(2, number): # индекс j от 2 до number
            if j <= i: # Если i индекс большеили равоно, пропускаем
                continue
            if number % (i + j) == 0: # Пароль складываветсчя из двух индексов50
                password += str(i) + str(j)
    return password

n = int(input('Введите целое число от 3 до 20: '))

result = get_password(n)
print('Пароль:', result)