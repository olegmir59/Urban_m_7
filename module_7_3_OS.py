#Домашнее задание по теме "Файлы в операционной системе".
#

import os
import time

directory = '.'
#directory = 'C:\\logs'
#directory = 'C:\\Projects\\Python\\Urban_2020_HW\\Module_7'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        secs = os.path.getmtime(filepath)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(file)
        parent_dir = os.path.dirname(__file__)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')