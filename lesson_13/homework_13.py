"""
++++++++++++++++++++++++++++++++++++++++++++++++
Декораторы в Python
++++++++++++++++++++++++++++++++++++++++++++++++
===============================================
1. Напишите декоратор uppercase_decorator, который делает результат выполнения функции прописными буквами.
Пример вызова:
@uppercase_decorator
def say_hello():
    return "hello, world!"
print(say_hello())  # "HELLO, WORLD!"
===============================================
"""
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Текст из функции: {result}')
        return f'Текст после выполнения декоратора {result.upper()}'
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello, world!"

print(say_hello())
print('------------------------------')

"""
2. Создайте декоратор repeat(n), который выполняет функцию n раз.
Пример вызова:
@repeat(3)
def hello():
    print("Hello!")
hello()
Вывод:
Hello!
Hello!
Hello!
===============================================
"""
print('Задание № 2')

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                # print(f'{i+1} вызов')
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello!")

hello()
print('------------------------------')

"""
3. Создайте декоратор cache, который кэширует результаты выполнения функции.
Если функция вызывается с теми же аргументами – возвращать сохраненный результат вместо нового вычисления.
Пример вызова:
@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b
print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
print(slow_add(2, 3))  # 5 (результат взят из кэша)
===============================================
"""
def cache(func): # Тут, конечно, я делал с помощью ИИ, слишком сложно на данном этапе для меня.
    cached_results = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cached_results:
            return f'{cached_results[key]} (результат взят из кэша)'
        result = func(*args, **kwargs)
        cached_results[key] = result
        return result
    return wrapper

@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}... ", end="")
    return a + b

print(slow_add(2, 3))
print(slow_add(2, 3))
print('------------------------------')

"""
4. Создайте декоратор с таймером timer(repeat), который выполняет функцию repeat раз и выводит среднее время выполнения.
Пример вызова:
@timer(3)
def slow_function():
    time.sleep(1)
slow_function()  # Среднее время выполнения: 1.0002 сек
"""
import time

def timer(repeat):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_time = 0
            for i in range(repeat):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                current_time += end_time - start_time
            srednee = current_time / repeat
            print(srednee)
            return result
        return wrapper
    return decorator


@timer(1)
def slow_function():
    time.sleep(1)

slow_function()