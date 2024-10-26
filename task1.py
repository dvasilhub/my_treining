# 1st program
N9 = int(input("Введите число:"))
Rez9 = (N9 * 5) ** 0.5
print("Результат: " + str(Rez9))

# 2nd program
if (9.99 > 9.98) and (1000 != 1000.1):
    print("Результат: True")

#3rd program
n = 2 * 2 + 2
print("Без приоритета: " + str(n))
n = 2 * (2 + 2)
print("С приоритетом: " + str(n))

#4th program
s = "123.456"
print(s[4])
ss = float("123.456")*10
print(str(ss))