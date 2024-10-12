# Домашнее задание по теме "Многопроцессное программирование"
# Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.
# Задача "Многопроцессное считывание":
import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, mode='r', encoding='utf8') as file:
        while True:
            # читаем одну строку
            line = file.readline()
            if not line:
                break
            all_data.append(line)


inp_files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

''''
time_start = datetime.now()

for fil_ in inp_files:
    read_info(fil_)

time_finish = datetime.now()
print("линейный вызов:")
print(time_finish - time_start)

'''

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        time_start = datetime.now()
        pool.map(read_info, inp_files)
    time_finish = datetime.now()
    print("многопроцессорный вызов")
    print(time_finish - time_start)
