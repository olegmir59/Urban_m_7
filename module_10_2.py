#  Домашнее задание по теме "Потоки на классах"
#  Цель: научиться создавать классы наследованные от класса Thread.
#
# Задача "За честь и отвагу!":

from time import sleep
from threading import Thread
from threading import Lock
lock = Lock()

class Knight(Thread):
    def __init__(self,  name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        count_of_enemy = 100
        days_of_war = 0
        print(f"{self.name}, на нас напали!")
        while count_of_enemy > 0:
            sleep(1)
            lock.acquire()
            count_of_enemy -= self.power
            days_of_war += 1
            print(f"{self.name} сражается {days_of_war} дней(дня)..., осталось {count_of_enemy} воинов.")
            lock.release()
        print(f"{self.name} одержал победу спустя  {days_of_war}  дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы закончились!")