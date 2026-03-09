#TASK_FUN_#1
#
# 1.	Напишите функцию m(a, b), вычисляющую минимум двух чисел.
# С помощью вашей функции найдите минимальное четырёх чисел.

def m(a, b):
    if a < b:
        return a
    else:
        return b
num_1 = int(input("Введи число №1: "))
num_2 = int(input("Введи число №2: "))
num_3 = int(input("Введи число №3: "))
num_4 = int(input("Введи число №4: "))

count_min_1 = m(num_1, num_2)
count_min_2 = m(num_3, num_4)
count_min_total = m(count_min_1, count_min_2)
print("Минимум из чисел: ",count_min_total)
#
# 2.	Дано натуральное число n > 1. Проверьте, является ли оно совершенным.
# Программа должна вывести слово YES, если число совершенное и NO, в противном случае.
#
def int_1(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n
n = int(input("Ввести число: "))
if int_1(n):
    print("YES")
else:
    print("NO")


# 3.	Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает
# n-e число Фибоначчи. Ищем число Фиббоначи через цикл! Рекурсию не использовать!

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    num_1 = 0
    num_2 = 1
    for i in range(2, n + 1):
        num_3 = num_1 + num_2
        num_1 = num_2
        num_2 = num_3
    return num_2
print(fibonacci(10))

# 4.	Напишите реализацию функции closest_mod_5,
# принимающую в качестве единственного аргумента целое число x
# и возвращающую самое маленькое целое число y, такое что:
# -y больше или равно x
# -y делится нацело на 5

def closest_mod_5(x):
    ostatok = x % 5
    if ostatok == 0:
        return x
    else:
        return x + (5- ostatok)
print(closest_mod_5(4))

# 6.	Сгенерировать список нечётных двузначных чисел.

def generate_digit():
    return [x for x in range(10, 100) if x % 2 != 0]
print(generate_digit())

# 7.	Сгенерировать список всех трёхзначных чисел кратных 5 и 3.

numbers = [n for n in range(100, 1000) if n % 5 == 0 and n % 3 == 0]
print("Трехзначные числа: ")
print(numbers)

# 8.	Дан список, упорядоченный по не убыванию элементов в нем. Напишите функцию
# которая определяет количество в нем различных элементов. set функцию не использовать.

def count_element(n):
    if not n:
        return 0
    count_1 = 1
    for item in range(1, len(n)):
        if n[item] != n[item - 1]:
            count_1 += 1
    return count_1
print(count_element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 9.	Напишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Для элементов списка, являющихся крайними, одним из соседей считается элемент,
# находящий на противоположном конце этого списка. Например, если на вход подаётся
# список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).Если
# на вход пришло только одно число, надо вывести его же. Вывод должен содержать одну
# строку с числами нового списка, разделёнными пробелом.
#
# Sample Input 1:
# 1 3 5 6 10
# Sample Output 1:
# 13 6 9 15 7
# Sample Input 2:
# 10
# Sample Output 2:
# 10
# Sample Input 3:
# 10 2
# Sample Output 3:
# 4 20

numbers = list(map(int, input("Введи числа списка через пробел: ").split()))
if not numbers:
    print("")
elif len(numbers) == 1:
    print(numbers[0])
else:
    result = []
    for item in range(len(numbers)):
        left = numbers[item - 1]
        right = numbers[(item + 1) % len(numbers)]
        result.append((left + right))
    print(" ".join(map(str, result)))



