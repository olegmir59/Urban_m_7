#  Домашнее задание по теме "Интроспекция"
# Цель задания:
#
# Закрепить знания об интроспекции в Python.
# Создать персональную функции для подробной интроспекции объекта.
#
# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа)
# в качестве аргумента и проводит интроспекцию этого объекта,
# чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
import inspect
import sys
from pprint import pprint

class Dog:
    def __init__(self, name, size, colour):
        self.name = name
        self.size = size
        self.colour = colour

    def run_dog(self):
        print("побежааааааааааал!")
    def sleep_dog(self):
        print("сплююююю, не будить!")

    def voice_dog(self):
        print("лаю!")
        return "Gaw Gaw Gaw"

def introspection_info(obj):
    print(f"Тип объекта: {type(obj)}")
    print(" ********  Атрибуты объекта (без методов): ")
    list_of_callable = []
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        if callable(attr):
            list_of_callable.append(attr_name + " Тип объекта: " + str(type(attr)))
        else:
            print(attr_name, " Тип объекта: ", type(attr))
    print(" ********  Методы объекта : ")
    for line in list_of_callable:
        print(line)
    print(f"Модуль, к которому объект принадлежит: {obj.__class__.__module__}")

    print(f"Размер  объекта: {sys.getsizeof(obj)}")


dog1 = Dog("Richard", 70, "red")
dog2 = Dog("Мефодий", 25, "карамель")

introspection_info(dog1)
introspection_info(dog2)

introspection_info(42)