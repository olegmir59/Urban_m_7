#  Домашнее задание по теме "Блокировки и обработка ошибок"
# Цель: освоить блокировки потоков, используя объекты класса Lock и его методы.
#
# Задача "Банковские операции":

from time import sleep
from threading import Thread
from threading import Lock
from random import randint
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        self.lock2 = Lock()

    def deposit(self):
        dep_num = 0
        while dep_num <= 100:
            dep_val = randint(50,500)
            sleep(0.001)
            self.balance += dep_val
            self.lock2.acquire()
            print(f"Пополнение: {dep_val}. Баланс: {self.balance}")
            dep_num += 1
            self.lock2.release()
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        take_num = 0
        while take_num <= 100:
            take_num += 1

            take_val = randint(50,500)
            sleep(0.001)
            if take_val <= self.balance:
                self.balance -= take_val
                self.lock2.acquire()
                print(f"Снятие: {take_val}. Баланс: {self.balance}")
                self.lock2.release()
            else:
                self.lock2.acquire()
                print(f"Запрос отклонён, недостаточно средств")
                self.lock2.release()
                if not self.lock.locked():
                    self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
