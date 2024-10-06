#Домашнее задание по теме "Итераторы"

#Цель: освоить механизмы работы итераторов и описания методов __next__ и __iter__. Закрепить навык создания и выбрасывания исключений.

#Задача "Range - это просто":

class StepValueError(ValueError):
    pass

class  Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        else:
            self.step = step
        self.pointer = None

    def __iter__(self):
        self.pointer = None
        return self

    def __next__(self):
        if self.pointer ==  None:  # начальный элемент итератора
            next_ind = self.start + self.step
            if (self.step > 0 and next_ind > self.stop) or (self.step < 0 and next_ind < self.stop):
                raise StopIteration()  # больше нечего возвращать
            else:
                self.pointer = self.start
                return self.pointer


        else:                   # последующие элементы  итератора
            ind_ = self.pointer
            step_ = self.step
            next_ind = ind_ + step_
            if (self.step > 0 and next_ind > self.stop) or (self.step < 0 and next_ind < self.stop):
                raise StopIteration()  # больше нечего возвращать
            else:
                self.pointer += self.step       # следующий шаг итерации
                return self.pointer
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()





