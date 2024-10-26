#1st program
n = int(input("Введите число: "))
n2 = (n ** 0.5) * 5 
print(str(n2))

# 2nd program
if (9.99 > 9.98) and (1000 != 1000.1):
    print("Результат: True")

#3rd program
n1 = 1234
n2 = 5678
n11 = str(n1)
n22 = str(n2)
print(n11[1] + n11[2] + " and " + n22[1] + n22[2])
sum = int(n11[1])*10+int(n11[2]) + int(n22[1])*10+int(n22[2])
print(sum)

#4th program
print(int(13.42) == int(42.13 * 100) % 100 or int(13.42 * 100) % 100 == int(42.13))

