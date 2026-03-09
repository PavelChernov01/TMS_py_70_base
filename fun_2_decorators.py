#FUN_2_DECORATORS.PY
from html.entities import name2codepoint

from task_fun_1 import result

# 1.	Написать декоратор log_result, который печатает результат
# выполнения функции. Применить к функции возведения числа в квадрат.

def log_result(func):
    def wrapper(x):
        result = func(x)
        print("Результат: ", result)
        return result
    return wrapper
def square(x):
    return x * x
square = log_result(square)
square(2)
square(3)

# 2.	Написать декоратор repeat(n), который повторяет вызов функции
# n раз и возвращает последний результат.

def repeat(n):
    def decorator(func):
        def wrapper(x):
            result = None
            for i in range(n):
                result = func(x)
            return result
        return wrapper
    return decorator
def square(x):
    return x * x
decorator_fun = repeat(3)
wrapper_fun = decorator_fun(square)
square = wrapper_fun
print(square(10))

# 3.	Написать декоратор bench, который измеряет ошибки: если функция
# завершилась ошибкой, вывести её тип и сообщение.

def bench(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка: {e}")
    return wrapper
@bench
def div(x, y):
    return x / y

div(5, 0)

# 4.	Дан список слов. Получить список их длин.

input_str = input("Ввести слова через пробел: ")
words = input_str.split()
length = []
for word in words:
    length.append(len(word))
print("Слова: ", words)
print("Длины: ", length)

# 5.	Дан список: ['apple', 'Banana', 'cherry', 'DATE'].
# Получите новый список, оставив только слова в нижнем регистре

words = ['apple', 'Banana', 'cherry', 'DATE']
lower_words = [word for word in words if word.islower()]
print("Исходник: ", words)
print("Нижний регистр: ", lower_words)

# 6.	Дан список кортежей (имя, возраст). Получите
# новый список, оставив кортеж в котором возраст > 18.

people = [("Ivan", 25), ("Pavel", 17), ("Max", 19), ("Anna", 15), ("Elena", 12)]
adults = []
for person in people:
    name = person[0]
    age = person[1]
    if age > 18:
        adults.append(person)
print("Полный список: ", people)
print("Старше 18 лет: ", adults)

# 7.	Дан список списков: [[1,2],[3,4],[5,6]].
# С помощью reduce объединить в один список: [1,2,3,4,5,6].

from functools import reduce
data = [[1, 2],[3, 4],[5, 6]]
result = reduce(lambda x, y: x + y, data)
print(result)

# 8.	Дан список ['cat','car','mouse','dog','snake','cow'].
# Получить словарь: {начальная буква: [слова...]}.

words = ['cats', 'car', 'mouse', 'dog', 'snake', 'cow']
result = {}
for word in words:
    first_letter = word[0]
    if first_letter not in result:
        result[first_letter] = [word]
    else:
        result[first_letter].append(word)
print(result)

# 9.	Дан список кортежей (товар, цена, количество).
# Получить список сумм: цена * количество.

products = [
    ("apple", 18, 2),
    ("banana", 14, 3),
    ("orange", 22, 1),
]

total_sum = []
for product in products:
    name = product[0]
    price = product[1]
    quantity = product[2]

    summa = price * quantity
    total_sum.append(summa)
print(products)
print(total_sum)
