"""Завдання 2. Обчислення визначеного інтеграла.

Ваше друге завдання полягає в обчисленні значення інтеграла функції 
методом Монте-Карло."""

import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції f(x)
def f(x):
    """Функція f(x) = x^2"""
    return x ** 2

# Межі інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислення визначеного інтеграла за допомогою функції quad
result, error = spi.quad(f, a, b)
print(f"Аналітичний інтеграл: {result}")

# Метод Монте-Карло для оцінки інтегралу
N = 10000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)  # Випадкові точки по x
y_random = np.random.uniform(0, b**2, N)  # Випадкові точки по y

# Визначення кількості точок під кривою
under_curve = y_random < f(x_random)
# Оцінка площі під кривою методом Монте-Карло
area_estimate = (b - a) * (b**2) * np.sum(under_curve) / N
print(f"Інтеграл методом Монте-Карло: {area_estimate}")

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)  # Створення діапазону значень для x
y = f(x)  # Обчислення значень функції f(x) для побудови графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)  # Діапазон значень для інтегрування
iy = f(ix)  # Обчислення значень функції f(x) в цьому діапазоні
ax.fill_between(ix, iy, color='gray', alpha=0.3)  # Заповнення області під кривою

# Додавання точок Монте-Карло на графік
ax.scatter(x_random, y_random, s=1, color='blue', alpha=0.5)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])  # Встановлення меж для осі x
ax.set_ylim([0, max(y) + 0.1])  # Встановлення меж для осі y
ax.set_xlabel('x')  # Підпис осі x
ax.set_ylabel('f(x)')  # Підпис осі y
ax.axvline(x=a, color='gray', linestyle='--')  # Вертикальна лінія на нижній межі інтегрування
ax.axvline(x=b, color='gray', linestyle='--')  # Вертикальна лінія на верхній межі інтегрування
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))  # Назва графіка
plt.grid()  # Додавання сітки на графік
plt.show()  # Відображення графіка
