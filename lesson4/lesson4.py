# 1. დაწერეთ პირობა, რომელიც გაარკვევს შემოტანილი ასო არის თანხმოვანი თუ ხმოვანი. მაგალითი:
# შემოიტანე სიმბოლო: ბ "ბ" თანხმოვანია
# =====================
# შემოიტანე სიმბოლო: ი "ი" ხმოვანია
# =====================

# xmovani = ["ა","ე","ი","ო","უ"]
# inp = input("შემოიტანეთ ანბანის სიმბოლო")
#
# if inp in xmovani:
#     print(f"xmovani: {inp}")
# elif inp not in xmovani:
#     print(f"tanxmovani: {inp}")




# 2. დაწერე პირობა რომელიც for ციკლის გამოყენებით გამოიტანს რიცხვებს 10-დან 0-მდე
# for i in range(10, 0, -1):
#     print(i, end=" ")
# print() # ერთ ხაზს ჩამოაგდებს და შემდეგ კოდს არ მიაბავს ამ კოდს

# # 0-ის ჩათვლით:
# for i in range(10, -1, -1):
#     print(i, end=" ")
# print() # ერთ ხაზს ჩამოაგდებს და შემდეგ კოდს არ მიაბავს ამ კოდს





# 3. დაწერეთ ციკლი რომელიც დაბეჭდავს ლისტში მყოფ უდიდეს 3 რიცხვს და მათ ინდექსებს
# import random
# lst = [random.randint(1,20) for _ in range(10)] # ქმნის და ინახავს random მონაცემებს [1,4,2,3,6,5]
# print(lst)
# მაგალითი:
# [3, 14, 4, 1, 2, 11, 12, 18, 7, 18]
# მონაცემი 1: 18
# მონაცემი 2: 18
# მონაცემი 3: 14

# max_three_numb = []
# for i in range(3):
#     value = max(lst) # უდიდესი მნიშვნელობაა
#     index = lst.index(value) # ეს ამ უდიდესი მნიშვნელობის ინდექსია, ლისტში ვიგებთ სადაც დგას ელემენტი
#
#     print(f"მონაცემი: {value} | ინდექსი: {index}")
#
#     max_three_numb.append(value)
#     lst.remove(value) # ეს უკვე ნაპოვნ ელემენტს ამოიღებს ლისტიდან რომ max ფუნქციამ აღარ აღიქვას იგივე რიცხვი
# print() # ახალ ხაზებზე რომ დაიწეროს





# 4. დაწერეთ ციკლი რომელიც დაბეჭდავს ოთხუთხედს “#” (ასეთს) მოცემული სიმაღლისა და სიგანის
# მიხედვით
# მაგალითი:
# width=5
# height=2
# # # # #
# # # # #

# for _ in range(height):
#     for _ in range(width):
#         print("#", end=" ")
#     print()

# -------------

# width=2
# height=5
# #
# #
# #
# #
# #

# for i in range(height):
#     for j in range(width):
#         print("#", end=" ")
#     print()





# 5. მომხმარებელს შემოყავს ორი რიცხვი x & y შექმენით ფუნქცია, რომელიც მიიღებს ამ ორ
# პარამეტრს და დაბეჭდავს ყველა არითმეტიკულ ოპერაციას მაგალითი:
# 5 + 2 = 7
# 5 - 2 = 3
# 5 * 2 = 10
# 5 / 2 = 2.5
# 5 // 2 = 2
# 5 % 2 = 1

# first_number = input(f"შემოიყვანეთ პირველი რიცხვი: ")
# while not first_number.isdigit():
#     first_number = input("შეიყვანე მხოლოდ რიცხვი! პირველი: ")
#
# second_number = input("შემოიყვანეთ მეორე რიცხვი: ")
# while not second_number.isdigit():
#     second_number = input("შეიყვანე მხოლოდ რიცხვი! მეორე: ")
#
# def calculate(first_number = "0", second_number = "0"):
#     first_number = int(first_number)
#     second_number = int(second_number)
#     operators_list = ["+", "-", "*", "/", "//", "%", "**"]
#
#     operator = input(f"აირჩიეთ ოპერატორი '+', '-', '*', '/', '//', '%', '**'")
#
#     while operator not in operators_list:
#         print("არასწორი ოპერატორი!")
#         operator = input(f"აირჩიეთ ოპერატორი '+', '-', '*', '/', '//', '%', '**'")
#
#     if operator in operators_list:
#         if operator == "+":
#             total = first_number + second_number
#         elif operator == "-":
#             total = first_number - second_number
#         elif operator == "*":
#             total = first_number * second_number
#         elif operator == "/":
#             total = first_number / second_number
#         elif operator == "//":
#             total = first_number // second_number
#         elif operator == "%":
#             total = first_number % second_number
#         elif operator == "**":
#             total = first_number ** second_number
#         else:
#             print("თქვენი არჩეული ოპერატორი არავალიდურია")
#     print(f"total: {total}")
#
# calculate(first_number, second_number)




# 6. გადააქციეთ დავალება #4 ფუნქციად, რომელსაც ექნება 2 პარამეტრი სიმაღლე, სიგანე

# def square(width = 0, heigth = 0):
#     for _ in range(heigth):
#         for _ in range(width):
#             print("#", end=" ")
#         print()
#
# square(5, 2)


# def square(width = 0, heigth = 0):
#     for _ in range(heigth):
#         for _ in range(width):
#             print("#", end=" ")
#         print()
#
# square(2, 5)





# 7. დაწერეთ ფუნქცია, რომელიც მიიღებს 2 პარამეტრს:
# სტრიქონს და სიმბოლოს ფუნქციამ უნდა დაითვალოს თუ რამდენჯერ გვხვდება სიმბოლო სტიქონში. მაგალითი:
# in_str("John and Jane Doe", "J")
# >>> Character "J" in given string: 2 times

# def counter_symbols(string, symbol):
#     counter = string.count(symbol)
#     print(f"Character {symbol} in given {string}: {counter} times")
#
# counter_symbols("John and Jane Doe", "J")





# 8. დაწერეთ ფუნქცია რომელიც დაითვლის სიტყვების რაოდენობას წინადადებაში. მაგალითი:
# wc("რამდენიმე სიტყვა რომლის დათვლასაც ვაპირებთ")
# >>> სიტყვების რაოდენობა წინადადებაში შეადგენს 5-ს.

# def word_count(word):
#     counter = len(word.split())
#     print(f"სიტყვების რაოდენობა წინადადებაში: '{word}' - შეადგენს {counter}-ს.")
#
# word_count("რამდენიმე სიტყვა რომლის დათვლასაც ვაპირებთ")




# 9. შექმენი თამაში hangman სიტყვის გამოცნობა…
# კომპიუტერი ირჩევს “შემთხვევით” სიტყვას და მომხმარებელს აქვს 10 ცდა სიტყვის გამოსაცნობად, მომხმარებელს
# აქვს ასოების ჩაწერის უფლება და ასევე სიტყვის ჩაწერის უფლება სრულად, თუ სიტყვას 10 ცდაში გამოიცნობს
# გამოიტანოს “გილოცავ” თუ ვერ გამოიტანოს “თქვენ დამარცხდით” თამაშის გამორთვა “exit”

# import random
#
# def hangman():
#     words = ["პროგრამირება", "კომპიუტერი", "ბრაუზერი", "ინტერნეტი", "პაროლი",
#              "დეველოპერი", "ალგორითმი", "სერვერი", "ლოგიკა", "პითონი"]
#     rand_word = random.choice(words)
#     print(rand_word)
#     counter = 10
#
#     while counter > 0:
#         customer_try = input(f"გამოიცანით სიტყვა, გაქვთ {counter} ცდა: ")
#
#         if customer_try.strip() != rand_word:
#             counter -= 1
#
#         if customer_try.strip() == rand_word:
#             print("გილოცავ")
#             break
#
#         if counter == 0:
#             print("თქვენ დამარცხდით")
#             break
#
# hangman()





# 10. შექმენი პატარა თამაში სადაც მომხმარებელს აქვს ორი არჩევანი “მარჯვენა” ან “მარცხენა” პროგრამამ შემთხვევითობის
# პრინციპით უნდა გაანაწილოს რომელია სწორი “მარჯვენა” თუ “მარცხენა”, თუ მომხმარებელი 5 ცდიდან ყველა სწორ
# მიმართულებას აირჩევს გამოიტანე “გამარჯვება” სხვა შემთხვევაში “შენ დამარცხდი”, თამაშის გამორთვა “exit
#
# import random
#
# def labirint():
#     start_game = True
#
#     while start_game:
#         counter = 5
#         rigth = "მარჯვენა"
#         left = "მარცხენა"
#
#         while counter > 0:
#             question_choose = input(
#                 f"თამაში დაიწყო, თქვენ გაქვთ {counter} დონე გასავლელი - "
#                 f"აირჩიეთ 'მარჯვენა' ან 'მარცხენა' (exit - თამაშიდან გასვლა): "
#             )
#
#             if question_choose == "exit":
#                 print(f"თქვენ გამოხვედით თამაშიდან")
#                 start_game = False
#                 break
#
#             if question_choose != "მარჯვენა" and question_choose != "მარცხენა":
#                 print("არასწორი არჩევანი! - 'მარჯვენა' ან 'მარცხენა'! ")
#                 start_game = False
#                 break
#
#             correct_rand_direct = random.randint(0,1)
#
#             if correct_rand_direct == 1:
#                 correct = rigth
#             else:
#                 correct = left
#
#             # print(f"სწორი პასუხი იყო: {correct}")
#
#             if question_choose != correct:
#                 start_game = False
#                 print("შენ დამარცხდი")
#                 break
#
#             counter -= 1
#
#         if not start_game:
#             break
#
#         if counter == 0:
#             print("გამარჯვება!")
#
#         start_game = False
#
# labirint()