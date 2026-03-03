#TASK_CLSSES_1.PY
#
# 1.	Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию
# изменения этих переменных. Добавить функцию, которая находит сумму значений этих
# переменных, и функцию которая находит наибольшее значение из этих двух переменных.

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Вывод на экран: {self.x}, {self.y}")

    def update(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print("Переменные изменены")

    def get_sum(self):
        s = self.x + self.y
        print(f"Сумма = {s}")
        return s

    def get_max(self):
        if self.x > self.y:
            print(f"Наибольшее = {self.x}")
            return self.x
        else:
            print(f"Наибольшее = {self.y}")
            return self.y
num = MyClass(x=7, y=3)
num.show()
num.update(8, 9)
num.get_sum()
num.get_max()

# 2.	Описать класс, реализующий десятичный счетчик, который может увеличивать или
# уменьшать свое значение на единицу в заданном диапазоне. Предусмотреть инициализацию
# счетчика значениями по умолчанию и произвольными значениями. Счетчик имеет два метода:
# увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние.
# Написать программу, демонстрирующую все возможности класса.

class Counter:
    def __init__(self, minimum = 0, maximum = 10, first_num = 0):
        self.minimum = minimum
        self.maximum = maximum

        if first_num < minimum:
            self.value = minimum
            print(f"Значение меньше, ставим {minimum}")
        elif first_num > maximum:
            self.value = maximum
            print(f"Значение больше, ставим {maximum}")
        else:
            self.value = first_num
    def up(self):
        if self.value < self.maximum:
            self.value += 1
            print(f"Увеличили: {self.value}")
        else:
            print(f"Достигли максимум: {self.value}")

    def down(self):
        if self.value > self.minimum:
            self.value -= 1
            print(f"Уменьшили: {self.value}")
        else:
            print(f"Достигли минимум: {self.value}")
    @property
    def current(self):
        return self.value

counter = Counter(1, 10, 1)
print(f"Старт: {counter.current}")
counter.up()
counter.down()

# 3.	Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов,
# поиска продуктов по названию, добавления их в магазин и удаления продуктов из него.
#
class Shop:
    def __init__(self):
        self.products = []

    def add(self, name, price, quantity):
        self.products.append([name, price, quantity])
        print(f"Добавлено: {name}")

    def remove(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(f"Удалено: {name}")
                return
        print(f"Не найдено: {name}")

    def search(self, name):
        found = []
        for product in self.products:
            if product[0] == name:
                found.append(product)
        return found

    def show(self):
        for product in self.products:
            print(f"{product[0]}: {product[1]}, {product[2]}")

shop = Shop()
shop.add(name="яблоки", price=50, quantity=10)
shop.add(name="апельсины", price=35, quantity=12)
shop.show()
shop.remove("апельсины")
shop.show()

# 4.	Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
# Каждая копилка имеет ограниченную вместимость, которая выражается
# целым числом – количеством монет(capacity -вместимость), которые можно
# положить в копилку. Класс должен поддерживать информацию о количестве
# монет в копилке, предоставлять возможность добавлять монеты в копилку и
# узнавать, можно ли добавить в копилку ещё какое-то количество монет, не
# превышая ее вместимость.
# Класс должен иметь следующий вид:
#
# class MoneyBox:
#     def__init__(self, capacity) :
#     #конструктор с аргументом- вместимость копилки
#     def can_add(self,v)
#     #True, если можно добавить v монет, False иначе
#     def add(self,v)
#     #положить v монет в копилку
#
# При создании копилки, число монет в ней равно 0.
# Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
#
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        self.coins += v
        print(f"Добавлено: {v} монет. Всего: {self.coins}")

piggy = MoneyBox(5)
print(piggy.can_add((3)))
piggy.add(3)
print(piggy.can_add(3))
piggy.add(2)
print(piggy.can_add(1))


