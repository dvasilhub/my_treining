class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print ("Такого этажа не существует")
        else:
            print (new_floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name},кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if not isinstance (other, House):
            raise ArithmeticError ("other должен быть  объектом House")
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if not isinstance (other, House):
            raise ArithmeticError ("other должен быть  int или объектом House")
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance (other, House):
            raise ArithmeticError ("other должен быть  объектом House")
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if not isinstance (other, House):
            raise ArithmeticError ("other должен быть  объектом House")
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if not isinstance (other, House):
            raise ArithmeticError ("other должен быть  объектом House")
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if not isinstance (other, House):
            raise ArithmeticError ("other должен быть объектом House")
        return self.number_of_floors != other.number_of_floors

    def __add__(self, valuo):
        if not isinstance (valuo, (int, House)):
            raise ArithmeticError ("valuo должен быть int или объектом House")
        self.number_of_floors = self.number_of_floors + valuo
        return House (self.name, self.number_of_floors)

    def __radd__(self, valuo):
        return House.__add__ (self, valuo)

    def __iadd__(self, valuo):
        return House.__add__ (self, valuo)


h1 = House ('ЖК Эльбрус', 10)
h2 = House ('ЖК Акация', 20)
print (h1)
print (h2)
print (h1 == h2)
h1 = h1 + 10
print (h1)
print (h1 == h2)
h1 += 10
print (h1)
h2 = 10 + h2
print (h2)
print (h1 > h2)
print (h1 >= h2)
print (h1 < h2)
print (h1 <= h2)
print (h1 != h2)