# 1.	Создайте класс RangeIterator, который реализует протокол итератора (__iter__, __next__).
# Итератор должен возвращать числа в заданном диапазоне с указанным шагом. После окончания
# итерации должно выбрасываться исключение StopIteration.
#
# class RangeIterator:
#     def __init__(self, start, stop, step=1):
#         self.current = start
#         self.stop = stop
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.step > 0 and self.current >= self.stop:
#             raise StopIteration
#         if self.step < 0 and self.current <= self.stop:
#             raise StopIteration
#
#         value = self.current
#         self.current += self.step
#         return value
#
# print("Числа от 1 до 5:")
# for i in RangeIterator(1,6):
#     print(i, end=" ")
import collections


# 2.	Напишите генераторную функцию fibonacci(limit),
# которая возвращает последовательность Фибоначчи до
# заданного предела. Генерация должна останавливаться,
# когда значение превышает limit.

# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a + b
#
# print("числа до 20:")
# for n in fibonacci(20):
#     print(n, end=" ")

# 3.	Создайте класс LogReader, который читает строки из источника данных
# и является итерируемым объектом.
# Класс должен:
# -	поддерживать перебор через for
# -	пропускать пустые строки
# -	возвращать строки по одной без загрузки всех данных в память
#
# class LogReader:
#     def __init__(self, source):
#         self.source = source
#         self.position = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.position < len(self.source):
#             line = self.source[self.position].strip()
#             self.position += 1
#             if line:
#                 return line
#         raise StopIteration
#
# logs = ["1", "", "2", "  ", "3"]
# reader = LogReader(logs)
#
# for log in reader:
#     print(log)


# 4.	Напишите генераторную функцию flatten(iterable),
# которая принимает вложенную структуру (списки внутри списков)
# и возвращает элементы в плоском виде.
# Решение должно корректно обрабатывать любую глубину вложенности.
# Simple input:
# [1, [2, 3], [[4], 5], 6]
# Simple Output:
# 1 → 2 → 3 → 4 → 5 → 6
#
# def flatten(items):
#     for item in items:
#         if type(item) is list:
#             for subitem in flatten(item):
#                 yield subitem
#         else:
#             yield item
#
# data = [1, [2, 3], [[4], 5], 6]
# for item in flatten(data):
#     print(item, end=" - ")


