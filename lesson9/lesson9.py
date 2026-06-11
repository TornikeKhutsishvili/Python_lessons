# 1. ამოცანა
# შექმენი კლასი BankAccount, რომელსაც ექნება: დახურული ატრიბუტები: __balance, __owner.
# მეთოდი deposit(amount) – თანხის დამატება. მეთოდი withdraw(amount) – თანხის გამოტანა (არ უნდა გადავიდეს მინუსში).
# მეთოდი get_balance() – მხოლოდ წაკითხვისთვის. დაწერე კოდი ისე, რომ მომხმარებელს პირდაპირ __balance-ზე წვდომა არ ჰქონდეს.

# class BankAccount:
#     def __init__(self, balance, owner):
#         self.__balance = balance
#         self.__owner = owner
#
#     @property
#     def get_balance(self):
#         return self.__balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"დაემატა {amount} ლარი.")
#         else:
#             print("შეიყვანეთ დადებითი თანხა!")
#
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"გატანილია {amount} ლარი.")
#         else:
#             print("არასაკმარისი ბალანსი!")
#
# account = BankAccount(1000, "Tornike")
# account.deposit(500)
# account.withdraw(300)
# print(f"მიმდინარე ბალანსი: {account.get_balance} ლარი.")



# 2. ამოცანა
# შექმენი კლასი ShoppingCart, რომელსაც ექნება: ატრიბუტი items (სიაში პროდუქტების რაოდენობა).
# __len__() დააბრუნებს პროდუქტების რაოდენობას. __eq__() ორი კალათის შედარება – აბრუნებს True, თუ რაოდენობა ტოლია.
# გააკეთე 2 კალათა და შეადარე. გააკეთე 3 კალათა და შეადარე. გააკეთე 4 კალათა და შეადარე.

# class ShoppingCart:
#     def __init__(self, items):
#         self.items = items
#
#     @property
#     def get_items(self):
#         return self.items
#
#     def __len__(self):
#         return len(self.items)
#
#     def __eq__(self, other):
#         return self.items == other.items
#
# # 2 კალათა
# cart1 = ShoppingCart(["Apple", "Banana"])
# cart2 = ShoppingCart(["Book", "Pen"])
# print(f"cart1 length: {len(cart1)}, cart2 length: {len(cart2)}")
# print(f"cart1 == cart2:", cart1 == cart2, "\n")
#
# # 3 კალათა
# cart3 = ShoppingCart(["TV", "Phone", "Laptop"])
# print(f"cart3 length: {len(cart3)}")
# print("cart1 == cart3:", cart1 == cart3, "\n")
#
# # 4 კალათა
# cart4 = ShoppingCart(["Book", "Pen"])
# print(f"cart4 length: {len(cart4)}")
# print("cart2 == cart4:", cart2 == cart4, "\n")



# 3. ამოცანა
# გამოიყენე @dataclass მოდული კლასის Book შესაქმნელად: ველები: title, author, year.
# დაამატე მეთოდი is_classic() → აბრუნებს True, თუ წელი < 1970. შექმენი რამდენიმე წიგნი და შეამოწმე ფუნქცია.

# from dataclasses import dataclass
#
# @dataclass()
# class Book:
#     title: str
#     author: str
#     year: int
#
#     def is_classic(self):
#         if self.year < 1970:
#             return True
#
# book1 = Book("წითელი და შავი", "სტენდალი", 1830)
# print(book1.title, "-", book1.is_classic())
#
# book2 = Book("სამოსელი პირველი", "გურამ დოჩანაშვილი", 1975)
# print(book2.title, "-", book2.is_classic())
#
# book3 = Book("1984", "ჯორჯ ორუველი", 1949)
# print(book3.title, "-", book3.is_classic())
#
# book4 = Book("ჯინსების თაობა", "დათო ტურაშვილი", 2001)
# print(book4.title, "-", book4.is_classic())
#
# book5 = Book("ოსტატი და მარგარიტა", "მიხაილ ბულგაკოვი", 1967)
# print(book5.title, "-", book5.is_classic())
#
# book6 = Book("ბუდენბროკები", "თომას მანი", 1901)
# print(book6.title, "-", book6.is_classic())



# 4. ამოცანა
# შექმენი კლასი Person, რომელსაც ექნება __del__() მეთოდი, რომელიც ბეჭდავს "Person removed" როცა ობიექტი წაიშლება.
# შექმენი ობიექტი, შემდეგ წაშალე del-ით და ნახე როგორ რეაგირებს garbage collector.

# import gc
#
# class Person:
#     total_created = 0
#     total_deleted = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.total_created += 1
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#     def __del__(self):
#         Person.total_deleted += 1
#         print(f"{self.name} removed")
#
# person1 = Person("Tornike", 25)
# person2 = Person("Tornike2", 26)
# person3 = Person("Tornike3", 27)
# person4 = Person("Tornike4", 28)
#
# print(person1)
# print(person2)
# print(person3)
# print(person4)
#
# del person2
# del person3
#
# # gc.collect()
#
# print("შეიქმნა:", Person.total_created)
# print("წაიშალა:", Person.total_deleted)
# print("დარჩა:", Person.total_created - Person.total_deleted)
# # ბოლოს როცა სრულდება ყველაფერი დარჩენილ ობიექტებსაც შლის, რადგან lifecycle-ი აკეთებს დასრულების შემდეგ cleanup-ს
# print(person1)
# print(person4)



# 5. ამოცანა
# შექმენი კლასი Temperature, რომელსაც ექნება: დახურული ატრიბუტი __celsius. get და set property °C-სთვის. fahrenheit
# property (read-only), რომელიც აბრუნებს °F. შექმენი ობიექტი, შეცვალე °C და შეამოწმე °F ავტომატურად იცვლება თუ არა.

# class Temperature:
#     def __init__(self, __celsius):
#         self.__celsius = __celsius
#
#     @property
#     def celsius(self):
#         return self.__celsius
#
#     @celsius.setter
#     def celsius(self, value):
#         self.__celsius = value
#
#     def calc_fahrenheit(self):
#         return (self.__celsius * 1.8) + 32
#
#     @property
#     def fahrenheit(self):
#         return self.calc_fahrenheit()
#
# temp = Temperature(35)
#
# print("Celsius:", temp.celsius)
# print("Fahrenheit:", temp.fahrenheit)
#
# # ცელსიუსის შეცვლა
# temp.celsius = 40
#
# print("\nშეცვლის შემდეგ:")
# print("Celsius:", temp.celsius)
# print("Fahrenheit:", temp.fahrenheit)



# 6. ამოცანა
# შექმენი კლასი CustomList, რომელიც: ინახავს ელემენტებს. __getitem__() – აბრუნებს ელემენტს ინდექსით.
# __setitem__() – ცვლის ელემენტს. __iter__() – Iterable უნდა იყოს. გამოიყენე for ციკლში შენი CustomList.

# class CustomList:
#     def __init__(self, items):
#         self.items = items
#
#     # ელემენტის მიღება ინდექსით
#     def __getitem__(self, index):
#         return self.items[index]
#
#     # ელემენტის შეცვლა ინდექსით
#     def __setitem__(self, index, value):
#         self.items[index] = value
#
#     # iterable რომ გახდეს
#     def __iter__(self):
#         return iter(self.items)
#
# my_list = CustomList([10, 20, 30, 40])
#
# # __getitem__
# print(f"მეორე ინდექსზე მდგომი: {my_list[1]}")
#
# # __setitem__
# my_list[1] = 99
# print(f"მეორე ინდექსზე მდგომი შეიცვალა: {my_list[1]}")
#
# for item in my_list:
#     print(f"საბოლოო შედეგი მასივის ელემენტები: {item}")



# 7. ამოცანა
# შექმენი კლასი Refrigerator, რომელსაც ექნება: ატრიბუტი items (სია).
# __contains__() – აბრუნებს True, თუ პროდუქტი მაცივარშია ("milk" in fridge). __str__() – "Fridge with N items".
# __del__() – "Fridge unplugged!". დაამატე პროდუქტები, შეამოწმე "milk" in fridge, დაბეჭდე ობიექტი და ბოლოს წაშალე.

# class Refrigerator:
#     def __init__(self, items = []):
#         self.items = items
#
#     def __contains__(self, item):
#         return item in self.items
#
#     def __str__(self):
#         return f"Fridge with {len(self.items)} items"
#
#     def __del__(self):
#         print("Fridge unplugged!")
#
# fridge = Refrigerator(["milk", "eggs", "butter"])
# # print(fridge)
#
# print("milk" in fridge)
# print("bread" in fridge)
# print(fridge)
# del fridge
# # print(fridge)



# 8. ამოცანა
# შექმენი კლასი FunnyCalculator, რომელსაც ექნება:
# __add__() – აბრუნებს "Why are you adding numbers? Just buy a calculator".
# __mul__() – აბრუნებს "Multiplication is too mainstream...".
# __truediv__() – თუ გაყოფ 0-ზე, ბეჭდავს "ZeroDivisionError? Nah, let’s just say infinity"
# __str__() – "I’m the funniest calculator in Python!". ცადე calc + 5, calc * 2, 10 / calc და ნახე რა მოხდება.

class FunnyCalculator:
    def __add__(self, other):
        return "Why are you adding numbers? Just buy a calculator."

    def __mul__(self, other):
        return "Multiplication is too mainstream..."

    def __truediv__(self, other):
        try:
            return "Division is emotionally complicated..."
        except ZeroDivisionError:
            return "ZeroDivisionError? Nah, let’s just say infinity"

    def __str__(self):
        return "I’m the funniest calculator in Python!"

calc = FunnyCalculator()

print(calc + 5)
print(calc * 2)
print(10 / 2)
# print(10 / 0)
print(calc)
