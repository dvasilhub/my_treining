#Задача "Матрица воплоти":
# Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список) размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.
# Опередяляем мунцию
def get_matrix(n, m, value):
    matrix = [] # определяем матрицу
    for a in range(0, n): # проходим по значению от 0 от n
        mat1 = [] # определяем матрицу
        for b in range(0, m): # проходим по значению от 0 от m
            mat1.append(value) # добавляем элемент value матрице mat1
        matrix.append(mat1) # добавляем элемент mat1 матрице matrix
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)



