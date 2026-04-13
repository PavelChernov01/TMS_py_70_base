from itertools import count

# Примечание:
# 1-5 задачи решаются с использованием файлов с расширением .txt
# 6-7 задачи создаёте файлы формата .json
# 8 -9 задачи решаеюся с использованием готовых текстовых файлов 8.txt и 9.txt
#
#
# 1.	Создать текстовый файл и записать в него 6 строк.
# Записываемые строки вводятся с клавиатуры.
#
file = open('file.txt', 'w', encoding='utf-8')

for i in range(6):
    s = input()
    file.write(s + "\n")

file.close()
print('done')

# 2.	В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.

file = open('file.txt', 'a')
print("Ввести 3 строки для добавления:")
for i in range(3):
    s = input()
    file.write(s + "\n")

file.close()
print("3 строки добавлены в файл")

# 3.	Дан текстовый файл. Подсчитать количество символов в нем. Без \n

file = open('file.txt', 'r', encoding = 'utf-8')
text = file.read()
file.close()

count = 0
for i in text:
    if i == '\n':
        count += 1
print(f"Количество символов в файле: {count}")

# 4.	Имеется текстовый файл, содержащий 5 строк. Переписать каждую
# из его строк в список в том же порядке.

file = open('file.txt', 'r', encoding = 'utf-8')
lines = file.readlines()
file.close()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip("\n")

print(lines)

# 5.	Имеется текстовый файл. Получить текст, в котором в конце
# каждой строки из заданного файла добавлен восклицательный знак.
#
# Simple Input
# Fas dsad asd
# Asda das dsad!
# Dasd dsad das
# Dasda asd asd das!
# Output:
# Asda das dsad!
# Dasda asd asd das!

with open('file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
with open('file.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        line = line.rstrip("\n")
        file.write(line + "!\n")

print('done')

# Примечание:
#
# 6-7 задачи создаёте файлы формата .json
#
# 6.	В справочной аэропорта хранится расписание вылета самолетов на следующие сутки. Для каждого рейса указаны номер рейса, пункт назначения, время вылета. Вывести все номера рейсов и время вылета самолета для заданного пункта назначения. Пример файла flights.json
# [
#   {
#     "flight_number": "SU123",
#     "destination": "Москва",
#     "departure_time": "08:30"
#   },
#   {
#     "flight_number": "FR456",
#     "destination": "Варшава",
#     "departure_time": "12:15"
#   },
#   {
#     "flight_number": "BT789",
#     "destination": "Москва",
#     "departure_time": "18:40"
#   }
# ]
# Simple Input:
# Москва
# Simple Output:
# SU123 08:30
# BT789 18:40


import json

flights = [
    {
        "flight_number": "SU123",
        "destination": "Москва",
        "departure_time": "08:30"
    },
    {
        "flight_number": "FR456",
        "destination": "Варшава",
        "departure_time": "12:15"
    },
    {
        "flight_number": "BT789",
        "destination": "Москва",
        "departure_time": "18:40"
    }
]
with open('file.json', 'w', encoding='utf-8') as file:
    json.dump(flights, file, ensure_ascii=False, indent=2)

print("json создан")

with open('file.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(data)
