from pprint import pprint


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}; {self.weight}; {self.category}')


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name not in self.get_products():
                file.write(product.__str__() + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')
        file.close

s1 = Shop()
p1 = Product('Картошка',  53.5, 'Vegitables')
p2 = Product('Спагетти', 3.6, 'Groceries')
p3 = Product('Попидоры', 5.7, 'Vegetables')
s1.add(p1, p2, p3)
s1.get_products()
print(p1)
print(p2)
print(p3)