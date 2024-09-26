#   Домашнее задание по теме "Позиционирование в файле".
#  Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта. Написать усовершенствованную функцию записи.

#  Задача "Записать и запомнить":

def custom_write(file_name, strings):
    file = open(file_name, mode='w', encoding='utf8')
    strings_positions = {}
    for i in range(len(strings)):
        ind_begin = file.tell()
        file.write(strings[i] + '\n')
        strings_positions.update({(i+1, ind_begin): strings[i]})
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)