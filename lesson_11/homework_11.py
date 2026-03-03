"""
++++++++++++++++++++++++++++++++++++++++++++++++
Функции в Python
++++++++++++++++++++++++++++++++++++++++++++++++
===============================================
1. Привет, <name>! Добро пожаловать!
Пример вызова:
greet("Анна")
Ожидаемый результат:
Привет, Анна! Добро пожаловать!
===============================================
"""
from lesson_8.homework_8 import result


def greet(name):
    print(f'Привет, {name}! Добро пожаловать!')
greet('Анна')
print('--------------')

"""
2. Напишите функцию square(num), которая принимает число и возвращает его квадрат.
Пример вызова:
print(square(5))
Ожидаемый результат:
25
===============================================
"""
def square(num):
    return num ** 2

print(square(5))
print('--------------')
"""
3. Создайте функцию is_even(num), которая возвращает True, если число четное, и False, если нечетное.
Пример вызова:
print(is_even(4))
print(is_even(7))
Ожидаемый результат:
True
False
===============================================
"""
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))
print('--------------')

"""
4. Напишите функцию repeat_string(text, times), которая повторяет строку text times раз.
Пример вызова:
print(repeat_string("Python", 3))
Ожидаемый результат:
PythonPythonPython
===============================================
"""
def repeat_string(text, times):
    res1 = text * times
    return res1

print(repeat_string("Python", 3))
print('--------------')
"""
5. Напишите функцию add(a, b), которая принимает два числа и возвращает их сумму.
Пример вызова:
print(add(3, 7))
Ожидаемый результат:
10
===============================================
"""
def add(a, b):
    sum1 = a + b
    return sum1

print(add(3, 7))
print('--------------')
"""
6. Напишите функцию get_max(a, b, c), которая возвращает максимальное из трех чисел.
Пример вызова:
print(get_max(10, 25, 7))
Ожидаемый результат:
25
===============================================
"""
def get_max(a, b, c):
    maxi = max(a, b, c)
    return maxi

print(get_max(10, 25, 7))
print('--------------')
"""
7. Создайте функцию calculate(a, b, operation), которая выполняет одну из операций:
"+" — сложение
"-" — вычитание
"*" — умножение
"/" — деление
Пример вызова:
print(calculate(10, 5, "+"))
print(calculate(10, 5, "*"))
Ожидаемый результат:
15
50
===============================================
"""
def calculate(a, b, operation):
    if operation == "+":
        res2 = a + b
    elif operation == "-":
        res2 = a - b
    elif operation == "*":
        res2 = a * b
    elif operation == "/":
        if b == 0:
            return 'Ошибка - деление на ноль'
        res2 = a / b
    else:
        res2 = 'Неизвестная операция'
    return res2

print(calculate(10, 5, "+"))
print(calculate(10, 5, "*"))
print('--------------')
"""
8. Создайте функцию reverse_string(text), которая принимает строку и возвращает её в обратном порядке.
Пример вызова:
print(reverse_string("Python"))
Ожидаемый результат:
nohtyP
===============================================
"""
def reverse_string(text):
    reversed_text = text[::-1]
    return reversed_text

print(reverse_string("Python"))
print('--------------')
"""
9. Создайте функцию compare_strings(s1, s2, ignore_case=True, ignore_spaces=True),
которая сравнивает две строки, убирая пробелы и регистр, если соответствующие параметры установлены в True.
Пример вызова:
print(compare_strings("Hello", " hello "))  # True
print(compare_strings("Hello", "HELLO", ignore_case=False))  # False
print(compare_strings("Hello ", "Hello", ignore_spaces=False))  # False
===============================================
"""
def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
    if ignore_spaces:
        s1 = s1.strip()
        s2 = s2.strip()
    if ignore_case:
        s1 = s1.lower()
        s2 = s2.lower()
    return s1 == s2

print(compare_strings("Hello", " hello "))
print(compare_strings("Hello", "HELLO", ignore_case=False))
print(compare_strings("Hello ", "Hello", ignore_spaces=False))
print('--------------')
"""
10. Напишите функцию summarize(*args), которая возвращает сумму всех переданных чисел.
Если переданы нечисловые значения, игнорируйте их.
Пример вызова:
print(summarize(1, 2, 3))           # 6
print(summarize(10, "abc", 5, 2))   # 17 (игнорируем "abc")
===============================================
"""
# def summarize(*args):
#     summa = 0
#     for arg in args:
#         if type(arg) == int or type(arg) == float:
#             summa += arg
#     return summa
# print(summarize(1, 2, 3))
# print(summarize(10, "abc", 5, 2))
# print('--------------')

def summarize(*args):
    summa = 0
    for arg in args:
        if type(arg) == int or type(arg) == float:
            summa += arg
    return summa

print(summarize(1, 2, 3))
print(summarize(10, "abc", 5, 2))
print('--------------')

"""
11. Напишите функцию create_profile(name, age, **extra),
которая принимает имя, возраст и дополнительные параметры
(например, city, job, hobby) и выводит информацию о пользователе.
Пример вызова:
create_profile("Иван", 30, city="Москва", job="Инженер")
Ожидаемый результат:
Профиль пользователя:
Имя: Иван
Возраст: 30
Дополнительная информация:
city: Москва
job: Инженер
===============================================
"""
def create_profile(name, age, **extra):
    print(f'Профиль пользователя\nИмя: {name}\nВозраст: {age}')
    if extra:
        print('Дополнительная информация:')
        for key, value in extra.items():
            print(f'{key}: {value}')

create_profile("Иван", 30, city="Москва", job="Инженер")
print('--------------')
"""
12. Напишите функцию process_orders(*orders, discount=0),
которая принимает список заказов (чисел) и применяет скидку.
Пример вызова:
print(process_orders(100, 200, 300, discount=10))
Ожидаемый результат:
Сумма заказа: 600
С учетом скидки: 540
===============================================
"""
def process_orders(*orders, discount=0):
    total = 0
    for order in orders:
        total += order
        if discount:
            total2 = total * (1 - (discount / 100))
    return f'Сумма заказа: {total}\nС учетом скидки {total2}'

print(process_orders(100, 200, 300, discount=10))
print('--------------')
"""
13. Создайте функцию merge_lists(*lists), которая объединяет несколько списков в один.
Пример вызова:
print(merge_lists([1, 2], [3, 4], [5, 6]))
Ожидаемый результат:
[1, 2, 3, 4, 5, 6]
===============================================
"""
def merge_lists(*lists):
    result = []
    for list in lists:
        result += list
    return result

print(merge_lists([1, 2], [3, 4], [5, 6]))
print('--------------')

"""
14. Создайте функцию merge_dicts(*dicts), которая объединяет несколько словарей в один.
При совпадении ключей используется последнее значение.
Пример вызова:
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}
print(merge_dicts(d1, d2, d3))
Ожидаемый результат:
{'a': 1, 'b': 3, 'c': 5, 'd': 6}
"""
def merge_dicts(*dicts):
    result = {}
    for dict in dicts:
        result |= dict
    return result

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}
print(merge_dicts(d1, d2, d3))