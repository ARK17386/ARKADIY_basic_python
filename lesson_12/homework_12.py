"""
++++++++++++++++++++++++++++++++++++++++++++++++
Лямбда-функции
++++++++++++++++++++++++++++++++++++++++++++++++
===============================================
1. Создайте lambda-функцию, которая возвращает квадрат числа.
===============================================
"""
kvadrat = lambda x: x ** 2
print(kvadrat(3))
print('---------------------')
"""
2. Создайте lambda-функцию, которая проверяет, является ли число четным.
===============================================
"""
chetn = lambda y: y % 2 == 0
print(chetn(4))
print('---------------------')
"""
3. Используйте lambda в sorted(), чтобы отсортировать список строк по последней букве.
Пример вызова:
words = ["banana", "apple", "cherry"]
print(sort_by_last_letter(words))
Ожидаемый результат:
['banana', 'apple', 'cherry']
===============================================
"""
def sort_by_last_letter(words):
    return sorted(words, key=lambda z: z[-1])
words = ["banana", "apple", "cherry"]
print(sort_by_last_letter(words))
print('---------------------')

"""
++++++++++++++++++++++++++++++++++++++++++++++++
Замыкания
++++++++++++++++++++++++++++++++++++++++++++++++
1. Создайте функцию multiply_by(n), которая принимает число n и возвращает вложенную функцию.
Вложенная функция должна принимать число x и возвращать его произведение на n.
Пример вызова:
times3 = multiply_by(3)
times5 = multiply_by(5)

print(times3(10))  # 30
print(times5(10))  # 50
"""
def multiply_by(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = multiply_by(3)
times5 = multiply_by(5)
print(times3(10))
print(times5(10))
print('---------------------')
"""
++++++++++++++++++++++++++++++++++++++++++++++++
2. Напишите функцию counter(start=0), которая возвращает вложенную функцию.
Каждый вызов вложенной функции должен увеличивать счетчик на 1.
Пример вызова:

c1 = counter(5)
c2 = counter()

print(c1())  # 6
print(c1())  # 7
print(c2())  # 1
print(c2())  # 2

Подсказка: используйте nonlocal
"""

def counter(start=0):
    x = start
    def schetchik():
        nonlocal x
        x += 1
        return x
    return schetchik

c1 = counter(5)
c2 = counter()
print(c1())  # 6
print(c1())  # 7
print(c2())  # 1
print(c2())  # 2
