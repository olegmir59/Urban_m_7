#  Домашнее задание по теме "Оператор "with".
#  Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.
#  Задача "Найдёт везде":
import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        for file_name_ in self.file_names:
            with open(file_name_, mode='r', encoding='utf8') as file:
                words_str = " ".join(file.readlines()).lower()
                print(words_str)
                new_s = ""
                for i in range(len(words_str)):
                    if words_str[i] in [',', '.', '=', '!', '?', ';', ':', ' - ', "\n"]:
                        continue
                    else:
                        new_s += words_str[i]
                all_words[file_name_] = new_s.split(" ")
                file.closed()

        return all_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
#print(finder2.find('TEXT')) # 3 слово по счёту
#print(finder2.count('teXT')) # 4 слова teXT в тексте всего