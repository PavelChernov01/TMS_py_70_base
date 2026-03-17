# TASK_clsses_2

# 1.	Создайте абстрактный класс PaymentMethod. Объявить абстрактный
# метод pay(amount). Реализовать минимум 3 класса-наследника с разной
# логикой оплаты. Обеспечить возможность работать с объектами через
# общий интерфейс.  Проверить полиморфное поведение при вызове pay
#
# class Payment:
#     def pay(self, amount):
#         raise NotImplementedError
#
# class Cash(Payment):
#     def pay(self, amount):
#         print(f"Наличка: {amount} руб.")
#
# class Card(Payment):
#     def pay(self, amount):
#         print(f"Карта: {amount} руб.")
#
# class Online(Payment):
#     def pay(self, amount):
#         print(f"Онлайн: {amount} руб.")
#
# print("Разные способы оплаты:")
#
# payment = [Cash(), Card(), Online()]
# for p in payment:
#     p.pay(100)

# 2.	Создайте абстрактный класс Notification. Объявите абстрактный метод
# send(message). Реализуйте минимум 3 класса-наследника, каждый из которых
# отправляет сообщение по-разному.
#
# class Notification:
#     def send(self, message):
#         raise NotImplementedError
#
# class Email(Notification):
#     def send(self, message):
#         print(f"Email: {message}")
#
# class SMS(Notification):
#     def send(self, message):
#         print(f"SMS: {message}")
#
# class MMS(Notification):
#     def send(self, message):
#         print(f"MMS: {message}")
#
# notification = [
#     Email(),
#     SMS(),
#     MMS(),
# ]
# for n in notification:
#     n.send("Hi!")

# 3.	Создайте класс User с ролью. Реализуйте policy-класс, определяющий
# доступ к методам. Создайте декоратор, который проверяет право пользователя
# на выполнение метода. Продемонстрируйте разрешённый и запрещённый доступ
# без if внутри метода.

# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
# class Policy:
#     def __init__(self):
#         self.rights = {
#             "read": ["user", "admin"],
#             "write": ["admin"]
#         }
#     def can(self, user, method):
#         return user.role in self.rights.get(method, [])
#
# policy = Policy()
# def check(method_name):
#     def decorator(func):
#         def wrapper(self, user, *args, **kwargs):
#             if policy.can(user, method_name):
#                 print(f"{user.name} is {method_name}")
#                 return func(self, user, *args, **kwargs)
#             else:
#                 print(f"{user.name} is not {method_name}")
#                 return None
#         return wrapper
#     return decorator
# class File:
#     @check("read")
#     def read(self, user):
#         print(" читает файл ")
#
#     @check("write")
#     def write(self, user):
#         print(" записывает файл ")
#
# user_1 = User("Ann", "admin")
# user_2 = User("Ivan", "user")
# file = File()
#
# file.read(user_1)
# file.read(user_2)
# file.write(user_1)
# file.read(user_2)

# 4.	Создай класс BankAccount, который имеет закрытый баланс __balance.
# Позволяет пополнять deposit и снимать withdraw деньгию. Не позволяет
# снимать больше, чем есть на счету. Вводит суточный лимит снятия (например, 5000).
# Сделайте ограничение по транзакциям, не более 3 – х
#
# class BankAccount:
#     def __init__(self, balance:float=0):
#         self.__balance = balance
#         self.daily_limit = 5000
#         self.withdrawals_today = 0
#         self.max_withdrawals = 3
#
#     def deposit(self, amount: float):
#         pass
#
#     def withdraw(self, amount: float):
#         pass
#
#     def get_balance(self):
#         pass
#
# class BankAccount:
#     def __init__(self, balance=0):
#         self.__balance = balance
#         self.withdrawals = 0
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Пополнение: {amount}, Баланс: {self.__balance}")
#         else:
#             print("Сумма должна быть больше 0")
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Сумма должна быть больше 0")
#         elif amount > self.__balance:
#             print(f"Недостаточно средств: {self.__balance}")
#         elif amount > 5000:
#             print("Лимит снятия 5000 в день!")
#         elif self.withdrawals >= 3:
#             print("Лимит 3 снятий в день!")
#         else:
#             self.__balance -= amount
#             self.withdrawals += 1
#             print(f"Снятие: -{amount}, Баланс: {self.__balance}, Снятий: {self.withdrawals}/3")
#
#     def show_balance(self):
#         print(f"Баланс: {self.__balance}")
#         return self.__balance
#
# account = BankAccount(10000)
#
# account.deposit(2000)
# account.withdraw(1500)
# account.withdraw(2000)
# account.withdraw(1000)
# account.withdraw(500)
# account.show_balance()



