#  Домашнее задание по теме "Режимы открытия файлов"
#  Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.
#
#  Задача "Учёт товаров":
#

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f"{self.name}, {self.weight}, {self.category}")

class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file_prod = open(self.__file_name,'r')
        lines = file_prod.readlines()
        for line in lines:
            print(line.strip())
        file_prod.close()
        return ""

    def add(self, *products):
        list_prod_names = []
        file_prod = open(self.__file_name, 'r+')
        lines = file_prod.readlines()
        for line in lines:
            line_w =line[0:line.find(',')].lstrip()
            list_prod_names.append(line_w)
        for product in products:
            if product.name in list_prod_names:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                line_ = product.__str__()+"\n"
                file_prod.write(line_)
        file_prod.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)   # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
