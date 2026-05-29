# 1. დაწერეთ პაროლის გენერატორი. დავალების შესრულებაში დაგეხმარებათ: random მოდული, while ან for ციკლი,
# list, სტრიქონის ფორმატირება. input ის მეშვეობით უნდა შეგვეძლოს მითითება რა სიგრძის პაროლი გვინდა და რა
# სიმბოლეობიდან გენერირდება იგი: პაროლის სიგრძეს ირჩევს მომხმარებელი, უნდა თუ არა სიმბოლოები, რიცხვები,
# დიდი/პატარა ასოები (ლათინურად) თუ ქართულს შემოიტანს უნდა დაუწერო რომ “შეიყვანე მხოლოდ ლათინური ასოები”

# import random # random მოდული გვჭირდება შემთხვევითი სიმბოლოს ასარჩევად
# import re # regex (pattern validation) გამოყენებისთვის
#
# LETTER_PATTERN = r"^[A-Za-z]+$" # ლათინური ასოების შემოწმების pattern
# SYMBOL_PATTERN = r"^[^A-Za-zა-ჰ0-9]+$" # სიმბოლოების შემოწმების pattern
# # თუ აქ რაც არის იმას ჩავწერთ არ უნდა იმუშაოს, ეს გულისხმობს ყველაფერს ამ პატერნში
# # ჩანაწერის გარდა (^A-Za-zა-ჰ0-9) - ^ ეს რომ აქვს წინ ეს ეუბნება ყველაფერი გარდა ამათი
#
# # პაროლის სიგრძის შეყვანა/შემოწმება
# while True:
#     try:
#         password_length = int(input("რა სიგრძის პაროლი გინდათ? (მინიმუმ 4): "))
#
#         if password_length < 4:
#             print("პაროლის სიგრძე უნდა იყოს მინიმუმ 4")
#         else:
#             break
#
#     except ValueError: # თუ მომხმარებელმა შეიყვანა არა-რიცხვი (მაგ: d)
#         print("შეიყვანე მხოლოდ რიცხვი")
#
#
# # პაროლში რიცხვების შეყვანა/შემოწმება
# while True:
#     password_numbers = input("რა რიცხვები გინდათ?: ")
#
#     if password_numbers == "":
#         password_numbers = ""
#         break
#
#     if password_numbers.isdigit():
#         break
#     else:
#         print("მხოლოდ რიცხვები არის დაშვებული (0-9)")
#
#
# # პაროლში სიმბოლოების შეყვანა/შემოწმება
# while True:
#     password_symbols = input("რა სიმბოლოები გინდათ?: ")
#
#     if password_symbols == "":
#         password_symbols = ""
#         break
#
#     if re.fullmatch(SYMBOL_PATTERN, password_symbols):
#         break
#     else:
#         print("მხოლოდ სიმბოლოებია დაშვებული (!@#$...) — ასო/რიცხვი აკრძალულია")
#
#
# # პაროლში დიდი/პატარა ასოების შეყვანა/შემოწმება
# while True:
#     password_chars = input("ჩაწერეთ სასურველი დიდი/პატარა ასოები '(ლათინურად)': ")
#
#     if re.fullmatch(LETTER_PATTERN, password_chars):
#         break
#     else:
#         print("შეიყვანე მხოლოდ ლათინური ასოები (A-Z ან a-z)")
#
# characters = password_chars + password_numbers + password_symbols
# password = ""
#
# for _ in range(password_length):
#     password += random.choice(characters)
#
# print("გენერირებული პაროლი:", password)




# 2. პაროლის შეფასება
# ამოცანა: მომხმარებლის შეყვანილი პაროლი შეაფასე 0–10 შკალით: სიგრძე, ციფრები, სიმბოლოები,
# დიდი/პატარა ასოები, განმეორებადი სიმბოლოების არსებობა. მოთხოვნები: გამოიტანე “weak/medium/strong”.

import re # regex (pattern validation) გამოყენებისთვის
user_password = input("გთხოვთ შეიყვანეთ პაროლი")

# strong პაროლი:
# - უნდა იყოს 8 სიმბოლოზე მეტი, - უნდა შეიცავდეს დიდ ასოს, - პატარა ასოს, - ციფრს, - სპეციალურ სიმბოლოს
# re.search() გამოიყენება ტექსტში კონკრეტული pattern-ის (ნიმუშის) მოსაძებნად.
strong_password = (
    len(user_password) > 8
    and re.search(r"[A-Z]", user_password)
    and re.search(r"[a-z]", user_password)
    and re.search(r"[0-9]", user_password)
    and re.search(r"[^A-Za-z0-9]", user_password)
)

# medium პაროლი:
# - უნდა იყოს 8 სიმბოლოზე მეტი, - უნდა შეიცავდეს დიდ ასოს, - უნდა შეიცავდეს ციფრს
medium_password = (
    len(user_password) > 8
    and re.search(r"[A-Z]", user_password)
    and re.search(r"[0-9]", user_password)
)

# weak პაროლი:
# - მხოლოდ სიგრძეს ამოწმებს და იწყება თუ არა ასეოებზე
week_password = user_password.startswith("[a-z]") and len(user_password) > 8

if strong_password:
    print("strong")
elif medium_password:
    print("medium")
elif week_password:
    print("weak")
else:
    print("your password doesn't match requirements")
















