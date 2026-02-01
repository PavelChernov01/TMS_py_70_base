# task loop_(07/01/2026)

# 1.	Дано число n. Вывести все числа от 1 до n.

n = int(input("число n: "))           # O(1)
for i in range(1, n + 1):             # O(N)
    print(i)                          # O(1)
#
# 2.	Вывести на экран число "10" 20 раз столбиком.

for item in range(20):        # O(1)
    print(10)                 # O(1)

#
# 3.	Дано число n. Посчитать сумму всех чётных чисел от 0 до n.

n = int(input("ввести число: "))      # O(1)
for i in range(1, n + 1):             # O(N)
    if i % 2 == 0:                    # O(1)
        print(i)                      # O(1)
#
# 4.	Дано натуральное число. Определить произведение цифр в нем которые кратны 2, кроме числа 0.

num_1 = int(input("Натуральное число: "))         # O(1)
num_3 = 1                                         # O(1)
for i in str(num_1):                              # O(N)
    num_2 = int(i)                                # O(1)
    if num_2 % 2 == 0 and num_2 != 0:             # 0(1)
        num_3 *= num_2                            # O(1)
print(num_3)                                      # O(1)
#
# # 5.	Дано натуральное число n. Вывести на экран факториал этого числа.
# Например: 5! = 1 * 2 * 3 * 4 * 5 = 120

num_1 = int(input("Число для вывода факториала: "))       # O(1)
num_2 = 1                                                 # O(1)
for i in range(1, num_1 + 1):                             # 0(N)
    num_2 *= i                                            # O(1)
print(num_2)                                              # O(1)

# 6.	Дано число n. Вывести на экран числа
# 1, 4, 9, 16, 25, ... которые меньше n.
# Sample Input :
# 15
# Sample Output :
# 1 4 9

number = int(input("Ввод числа number: "))            # O(1)
for i in range(1, number + 1):                        # 0(N)
    if i ** 2 <= number:                              # 0(1)
        print(i**2, end=" ")                          # 0(1)
    else:
        break                                         # O(1)
#
# 7.	Дано число n. Найти сумму цифр в этом числе.

num_1 = input("Ввод числа для суммы цифр: ")          # O(1)
num_2 = 0                                             # O(1)
for i in num_1:                                       # O(N)
    num_2 += int(i)                                   # O(1)
print(num_2)                                          # O(1)

# 8.	Дано натуральное число n.
# Найти значение минимальной цифры в данном числе .

num_1 = input("Натуральное число: ")              # O(1)
max_num = 9                                       # O(1)
for i in str(num_1):                              # O(N)
    num_2 = int(i)                                # O(1)
    if num_2 < max_num:                           # O(1)
        max_num = num_2                           # O(1)
print(max_num)                                    # O(1)

# 9.	Дан текст. Написать программу, вставляющую после каждой запятой по одному пробелу.
# Если в тексте встречается два и более пробелов, требуется оставить один.

text_old = input("ввести текст, расставить пробелы: ")    # O(1)
text_new = text_old.replace(",", ", ")                    # O(N)
while "  " in text_new:                                   # O(N)
    text_new = text_new.replace("  ", " ")                # O(N)
while " ," in text_new:                                   # O(N)
    text_new = text_new.replace(" ,", ",")                # O(N)
print(text_new)                                           # O(1)

# 10.	С клавиатуры вводится натуральное число n <= 1000. Выведите n строк вида
# "На лугу n коров", склоняя слово "коров" в соответствии с числом n.
# Проверяем большие числа!!!
# Sample Input:
# 6
# Sample Output:
# На лугу 1 корова
# На лугу 2 коровы
# На лугу 3 коровы
# На лугу 4 коровы
# На лугу 5 коров
# На лугу 6 коров

n = int(input("Ввести число n<1000: "))   # O(1)
for i in range(1, n + 1):                 # O(N)
    if 11 <= i % 100 <= 19:               # O(N)
        print("На лугу", i, "коров")      # O(1)
    elif i % 10 == 1:                     # O(1)
        print("На лугу", i, "корова")     # O(1)
    elif i % 10 == 2:                     # O(1)
        print("На лугу", i, "коровы")     # O(1)
    elif i % 10 == 3:                     # O(1)
        print("На лугу", i, "коровы")     # O(1)
    elif i % 10 == 4:                     # O(1)
        print("На лугу", i, "коровы")     # O(1)
    else:
        print("На лугу", i, "коров")      # O(1)

# 11.	Узнав, что ДНК не является случайной строкой, только что поступившие в Институт
# биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия,
# который сжимает повторяющиеся символы в строке. Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки
# заменяются на этот символ и количество его повторений в этой позиции строки. Напишите программу,
# которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную
# последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
# Sample Input 1:
# Aaaabbcaa
# Sample Output 1:
# a4b2c1a2
# Sample Input 2:
# Abc
# Sample Output 2:
# a1b1c1

s = "aaaabbcaacccuureeer"                         # O(1)
s += " "                                          # O(1)
new_decoded_s = ""                                # O(1)
counter = 1                                       # O(1)
for ind in range(len(s) - 1):                     # O(N)
    if s[ind] == s[ind+1]:                        # O(N)
        counter += 1                              # O(1)
    else:
        new_decoded_s += s[ind] + str(counter)            # O(N)
        counter = 1                                       # O(1)
print(new_decoded_s)                                      # O(1)


# HOMETASK_4_(11/01/2026)

# 1.	Дан кортеж. Найти разность между его максимальным и минимальный элементом.

tuple_1 = (1, 2, 3, 3.14, -1, 0)                  #O(1)
max_num = tuple_1[0]                              #O(1)
min_num = tuple_1[0]                              #O(1)
for i in tuple_1:                                 #O(N)
    if i > max_num:                               #O(1)
        max_num = i                               #O(1)
    if i < min_num:                               #O(1)
        min_num = i                               #O(1)
        print("Разница= ", max_num - min_num)     #O(1)

# 2.	Дан кортеж. Написать программу, определяющую
# сколько раз менялся знак в кортеже. (5,2,-2,7,-8,-9,1) 4 раза

tuple_1 = (5,2,-2,7,-8,-9,1)                      #O(1)
num_mark = 0                                      #O(1)
for item in range(1, len(tuple_1)):               #O(N)
    if tuple_1[item-1] * tuple_1[item] < 0:       #O(1)
        num_mark += 1                             #O(1)
print("Смена знака: ", num_mark)                  #O(1)
# #
# 3.	Дан кортеж. Вывести на экран все простые числа в данном кортеже.

tuple_1 = tuple(map(int, input("Ввести кортеж через пробел: ").split()))      #O(N)
for item in tuple_1:                                                          #O(N)
    if item > 1:                                                              #O(1)
        print(item, end=" ")                                                  #O(1)
    elif item == 1:                                                           #O(1)
        print(item, end=" ")                                                  #O(1)
    else:
        print("", end=" ")                                                    #O(1)

# 6.	Задано два списка. Найти наименьшие среди элементов
# первого списка, которые не входят во второй список.
# [4,1,6,9]  [8,1,2,4,9,5,7,6] -> нет такого элемента

list_1 = [4, 1, 6, 9]             #O(1)
list_2 = [8, 1, 2, 4, 9, 5,7,6]   #O(1)
list_3 = []                       #O(1)
for item in list_1:               #O(N)
    if item not in list_2:        #O(N)
        list_3.append(item)       #O(1)
if list_3:
    minimum = list_3[0]           #O(1)
    for item in list_3[1:]:       #O(N)
        if item < minimum:        #O(1)
            minimum = item        #O(1)
    print(minimum)                #O(1)
else:
    print("нет такого элемента")  #O(1)


# 7.	Дан список положительных целых чисел .
# Вставить после каждого чётного числа его перевёртыш.
# 18 81, 42 24, 8 8, 122 221

input_string = input("ввести данные через пробел: ")  #O(1)
num_1 = list(map(int, input_string.split()))          #O(N)
num_2 = []                                            #O(1)
for item in num_1:                                    #O(N)
    num_2.append(item)                                #O(1)
    if item % 2 == 0:                                 #O(1)
        num_3 = int(str(item)[::-1])                  #O(1)
        num_2.append(num_3)                           #O(1)
print(num_2)                                          #O(1)
couple = []                                           #O(1)
for item in num_2:                                    #O(N)
    item_str = str(item)                              #O(1)
    if item_str[0] != item_str[-1]:                   #O(N)
        couple.append(item)                           #O(1)
print(couple)                                         #O(1)

# 8.	Дан список . Вычислить сколько раз в нем встречается каждый элемент,
# не используя сортировки. [5,2,4,5,1,2] 1 – 1 2 – 2 4 – 1 5 - 2

list_num_1 = [5, 2, 4, 5, 1, 2]                       #O(1)
list_num_2 = []                                       #O(1)
for item in list_num_1:                               #O(N)
    if item not in list_num_2:                        #O(N)
        answer = list_num_1.count(item)               #O(N)
        print(item, "-", answer, ";", end=" ")        #O(1)
        list_num_2.append(item)                       #O(1)

# 11.	Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке), если это число
# ранее встречалось в последовательности или NO, если не встречалось.

list_num_1 = input("Ввести числа через пробел: ")     #O(1)
num_1 = list(map(int, list_num_1.split()))            #O(N)
list_num_2 = []                                       #O(1)
for item in num_1:                                    #O(N)
    if item in list_num_2:                            #O(N)
        print("YYES")                                 #O(1)
    else:
        print("NO")                                   #O(1)
        list_num_2.append(item)                       #O(1)

# 13.	Создайте словарь, связав его с переменной school, и наполните
# данными, которые бы отражали количество учащихся в разных 9 классах
# (9а, 9б, 9в, 9м, 9ф и т. п.). Внесите изменения в словарь согласно следующему:
# а) в одном из классов изменилось количество учащихся
# б) в школе появился новый класс.
# в) в школе был расформирован (удален) другой класс.
# г) Вычислите общее количество учащихся 9 классов в школе.

school = {'9а': 20, '9б': 25, '9в': 28, '9м': 21, '9ф': 29}       #O(1)
print(school)                                                     #O(1)
school['9в'] = 31                 #O(1)
school['9г'] = 19                 #O(1)
del school ['9ф']                 #O(1)
all_students = 0                  #O(1)
for item in school.values():      #O(N)
    all_students += item          #O(1)
print(all_students)               #O(1)


# 14.	Стремясь стать программистом, важно не
# только постоянно учиться, но и понимать язык,
# на котором говорят Ваши коллеги.

phrase = {}                                   #O(1)
print("Ввести опредение с точкой: ")          #O(1)
while True:                                   #O(N)
    after_point = input()                     #O(1)
    if after_point == '.':                    #O(N)
        break                                 #O(1)
    if " – " in after_point:                  #O(N)
        parts = after_point.split(" – ", 1)   #O(N)
        first_part = parts[0]                 #O(1)
        last_part = parts[1]                  #O(1)
        phrase[first_part] = last_part        #O(1)
m = int(input("Запрос: "))                    #O(1)
for item in range(1, m + 1):                  #O(N)
    word = input()                            #O(1)
    if word in phrase:                        #O(N)
        print(phrase[word])                   #O(1)
    else:
        print("Не найдено")                   #O(1)

# LESSON 8_(17/01/2026)

# 1.	Опишите конструкцию отлова ошибок, так чтобы выводило,
# какую ошибку вы сделали. Код представлен ниже:
# x = (1, 2, 5, 7)
# x = x  / 2
# print(x)

try:                        # O(1)
    x = (1, 2, 5, 7)        # O(1)
    x = x/2                 # O(1)
except Exception as exc:    # O(1)
    print("error =", exc)   # O(1)

# 2.	Напишите программу которые будет ловить IndexError, когда
# вы пытаетесь взять индекс элемента, которого нет в списке.

list_1 = [1, 2, 3]             # O(1)
try:                           # O(1)
    print(list_1[5])           # O(1)
except IndexError:             # O(1)
    print(" Ошибка - число не в диапазоне")     # O(1)

# 3.	Напишите программу которая вычисляет площадь треугольника по формуле Герона,
# однако если пользователь введёт длину хоть одной стороны треугольника равную 0, то
# программа должна бросить исключение ArithmeticError.

a = float(input("side_1: "))                # O(1)
b = float(input("side_2: "))                # O(1)
c = float(input("side_3: "))                # O(1)

if a == 0 or b == 0 or c == 0:              # O(1)
    raise ArithmeticError("it's zero!")     # O(1)
if a + b <= c or b + c <= a or c + a <= b:  # O(1)
    print("The triangle does not exist")    # O(1)
else:                                       # O(1)
    p = (a + b + c) / 2                     # O(1)
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5    # O(1)
    print(s)                                        # O(1)

# 4.	Дан список. Пользователь не знает его размер. Программа должна бросить исключение
# TypeError, когда пользователь пытается удалить элемент которого нет в списке.

list_task_4 = [1, 2, 3, 4]                # O(1)
num_4 = int(input("Enter number: "))      # O(1)
if num_4 in list_task_4:                  # O(N)
    list_task_4.remove(num_4)             # O(N)
    print("delete item:", list_task_4)    # O(N)
else:
    print("another number")               # O(1)

# 5.	Дан словарь, который содержит некоторые ключи и значения по этим ключам,
# пользователь не знает этих ключей. Бросьте ошибку KeyError в том случае когда
# пользователь пытается просмотреть значение по ключу, которого нет в словаре.

dictionary_1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}   # O(1)
key_1 = input("Enter a key : ")                           # O(1)
try:
    print(dictionary_1[key_1])                            # O(1)
except KeyError:                                          # O(1)
    raise KeyError("Key not found")                       # O(1)

# 6.	Дана строка, содержащая числа, разделённые пробелами. Нужно вывести их сумму.
# Если хотя бы один элемент не является числом — перехватить исключение и пропустить его.
# "10 5 abc 3" → 18

str_1 = "10 5 abc 3"                      # O(1)
sum_int = 0                               # O(1)
for item in str_1.split():                # O(N)
    try:
        sum_int = sum_int + int(item)     # O(1)
    except ValueError:                    # O(1)
        pass
print(sum_int)                            # O(1)


