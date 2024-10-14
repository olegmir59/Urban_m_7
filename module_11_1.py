#  Домашнее задание по теме "Обзор сторонних библиотек Python"
# Цель: познакомиться с использованием сторонних библиотек в Python и применить их в различных задачах.

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.

x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) Axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()

np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
plt.show()

x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сетнябрь', 'Октябрь']
y = [70, 47, 20, 21, 17, 15, 20, 21, 14, 46]

plt.bar(x, y, label='Величина прибыли Светотехника')
plt.plot(x, y, color='green', marker='o', markersize=7)

plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в тыс руб.')
plt.title('Комбинирование графиков')
plt.legend()
plt.show()
