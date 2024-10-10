#  Домашнее задание по теме "Очереди для обмена данными между потоками."
#  Цель: Применить очереди в работе с потоками, используя класс Queue.
#
# Задача "Потоки гостей в кафе":

import time
from collections import defaultdict

import queue
import random
import threading


class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None


class Guest:
    def __init__(self,name):
        self.name = name

    def run(self):
        guest_move_time = random.randint(3,10)
        time.sleep(guest_move_time)


class Cafe:
    def __init__(self,*tables):
        self.tables = tables
        self.cafe_queue = queue.Queue(maxsize=20)
    def guest_arrival(self, *guests):
        for guest_in in guests:
            find_a_free_table =False
            for table in self.tables:
                if table.guest == None:
                    table.guest = guest_in
                    find_a_free_table = True
                    break
            if not find_a_free_table:
                self.cafe_queue.put(guest_in)

