#  Домашнее задание по теме "Создание потоков".
# Если вы решали старую версию задачи, проверка будет производиться по ней.
# Ссылка на старую версию тут.
# Цель: понять как работают потоки на практике, решив задачу
#
# Задача "Потоковая запись в файлы":

from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with (open(file_name, mode='w', encoding='utf8') as file):
        for i in range(1,word_count+1):
            file.write("Какое-то слово № " + str(i) + "\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

time_start = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
time_end = datetime.now()
print(f"Работа потоков: {time_end - time_start}")

tr_1 =Thread(target=write_words, args=(10, "example5.txt"))
tr_2 =Thread(target=write_words, args=(30, "example6.txt"))
tr_3 =Thread(target=write_words, args=(200, "example7.txt"))
tr_4 =Thread(target=write_words, args=(100, "example8.txt"))

time_start = datetime.now()

tr_1.start()
tr_2.start()
tr_3.start()
tr_4.start()

tr_1.join()
tr_2.join()
tr_3.join()
tr_4.join()

time_end = datetime.now()
print(f"Работа потоков: {time_end - time_start}")