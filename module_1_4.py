my_string = input("Введите любой текст через пробелы: ") # Создайте переменную my_string и присвойте ей значение строки с произвольным текстом
print("Количество символов в тексте:", str(len(my_string))) # 
print("Текст в верхнем регистре:", my_string.upper()) # 
print("Текст в нижнем регистре:", my_string.lower()) # 
my_string = my_string.replace(' ', '') # 
print("Текст без пробелов:", my_string) # 
print("Первый символ:", my_string[0]) # 
print("Последний символ:", my_string[-1]) # 