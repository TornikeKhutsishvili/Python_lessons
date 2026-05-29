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

# import re # regex (pattern validation) გამოყენებისთვის
# user_password = input("გთხოვთ შეიყვანეთ პაროლი")
#
# # strong პაროლი:
# # - უნდა იყოს 8 სიმბოლოზე მეტი, - უნდა შეიცავდეს დიდ ასოს, - პატარა ასოს, - ციფრს, - სპეციალურ სიმბოლოს
# # re.search() გამოიყენება ტექსტში კონკრეტული pattern-ის (ნიმუშის) მოსაძებნად.
# strong_password = (
#     len(user_password) > 8
#     and re.search(r"[A-Z]", user_password)
#     and re.search(r"[a-z]", user_password)
#     and re.search(r"[0-9]", user_password)
#     and re.search(r"[^A-Za-z0-9]", user_password)
# )
#
# # medium პაროლი:
# # - უნდა იყოს 8 სიმბოლოზე მეტი, - უნდა შეიცავდეს დიდ ასოს, - უნდა შეიცავდეს ციფრს
# medium_password = (
#     len(user_password) > 8
#     and re.search(r"[A-Z]", user_password)
#     and re.search(r"[0-9]", user_password)
# )
#
# # weak პაროლი:
# # - მხოლოდ სიგრძეს ამოწმებს და იწყება თუ არა ასეოებზე
# week_password = user_password.startswith("[a-z]") and len(user_password) > 8
#
# if strong_password:
#     print("strong")
# elif medium_password:
#     print("medium")
# elif week_password:
#     print("weak")
# else:
#     print("your password doesn't match requirements")




# 3. დაწერე ფუნქცია (ფიბონაჩის რიგი) - *რა არის ფიბონაჩი - ბოლო ორი ელემენტის ჯამით ვამატებთ
# ახალ რიცხვს*, სანამ სიგრძე არ გახდება მომხმარებლის მიერ შემოყვანილი რიცხვი, აუცილებლად
# უნდა შემოიტანოს რიცხვი, სხვა რამის შემოტანის დროს უნდა შემოწმდეს რა შემოიტანა
# მომხმარებელმა და უნდა დაუსახელო აღნიშნული და უთხრა რომ მხოლოდ რიცხვი შემოიტანოს. მაგ:
# შემოიტანა სიმბოლო, უნდა უთხრა შენ შემოიტანე სიმბოლო არასწორია, მხოლოდ რიცხვი!

# def fibonacci_row():
#     user_input = input("შეიყვანეთ რიცხვი: ")
#
#     if user_input.isdigit():
#         number = int(user_input)
#
#         fibonacci = [0, 1] # ფიბონაჩის საწყისი სია
#
#         if number == 1: # თუ მომხმარებელმა შეიყვანა 1
#             print([0])
#         elif number == 2: # თუ მომხმარებელმა შეიყვანა 2
#             print(fibonacci)
#         else:
#             # სანამ სიის სიგრძე არ გაუტოლდება მომხმარებლის რიცხვს
#             while len(fibonacci) < number:
#                 # ბოლო ორი ელემენტის ჯამი
#                 next_number = fibonacci[-1] + fibonacci[-2]
#
#                 # ახალი რიცხვის დამატება სიაში
#                 fibonacci.append(next_number)
#
#             # შედეგის დაბეჭდვა
#             print(fibonacci)
#     else:
#         # ვამოწმებთ რა ტიპის სიმბოლო შემოიტანა მომხმარებელმა
#         # თუ ასოები შეიყვანა
#         # isalpha() - ვამოწმებთ ასოებზე, სტრინგი შედგება მხოლოდ: A-Z a-z
#         if user_input.isalpha():
#             print("თქვენ შემოიტანეთ ასოები, მხოლოდ რიცხვი შეიყვანეთ!")
#
#         # თუ სპეციალური სიმბოლოები შეიყვანა
#         # isalnum() - ვამოწმებთ სიმბოლოებზე, ამოწმებს სტრინგი შედგება თუ არა ასოებისგან და რიცხვებისგან
#         # ამ შემთხვევაში not -ი მიუთითებს რომ თუ არც ასოებს და არც რიცხვებს არ შეიცავს მაშინ სხვა სიმბოლოებია
#         elif not user_input.isalnum():
#             print("თქვენ შემოიტანეთ სიმბოლოები, მხოლოდ რიცხვი შეიყვანეთ!")
#
#         # სხვა არასწორი შემთხვევა
#         else:
#             print("არასწორი მონაცემი, მხოლოდ რიცხვი შეიყვანეთ!")
#
#
# fibonacci_row()




# 4. პალინდრომი
# ამოცანა: შეამოწმე, არის თუ არა შეყვანილი ტექსტი პალინდრომი (მხოლოდ ასოები/ციფრები). თუ
# არაა, შესთავაზე ყველაზე ახლო პალინდრომი ერთი სიმბოლოს ჩასმით/წაშლით.

# import re # regex (pattern validation) გამოყენებისთვის
# from random import randint
#
# LETTER_PATTERN = r"^[A-Za-z0-9]"
# palindrom_input = input("შეიყვანეთ პალინდრომი")
#
# # დავტოვებთ მხოლოდ ასოებს და ციფრებს
# text = re.sub(LETTER_PATTERN, '', palindrom_input).lower()
# # re.sub() - ტექსტის შეცვლისთვის (replace), პოულობს კონკრეტულ pattern-ს და ცვლის სხვა ტექსტით
#
# # ვამოწმებთ არის თუ არა პალინდრომი
# if text == text[::-1]:
#     print("ეს არის პალინდრომი")
# else:
#     print("ეს არ არის პალინდრომი")
#
#     # 3. ვპოულობთ ყველაზე ახლო ვერსიას - ვცდილობთ ერთი სიმბოლოს წაშლით პოვნას
#     found = False
#
#     for i in range(len(text)):
#         test = text[:i] + text[i+1:]
#
#         if test == test[::-1]:
#             print("ახლოსაა პალინდრომთან (ერთი სიმბოლოს წაშლით):", test)
#             found = True
#             break
#
#     if not found:
#         print("ერთ სიმბოლოს წაშლით ვერ გასწორდა")




# 5. ზედმეტსახელების გენერატორი
# მომხმარებელს შემოაქვს მხოლოდ ერთი სიტყვა (სხვა შემთხვევები დაბლოკე) და შენ სთავაზობ 5
# ზედმეტსახელს ამ სიტყვასთან კავშირში.

# import random
# customer_word = input("შემოიყვანეთ მხოლოდ ერთი სიტყვა")
#
# # ვამოწმებთ არის თუ არა ერთი სიტყვა
# if len(customer_word.split()) == 1 and customer_word.isalpha():
#     nicknames = []
#
#     for i in range(5):
#         number = random.randint(1, 100)
#         nickname = customer_word + str(number)
#         nicknames.append(nickname.strip())
#
#     print("შენი ზედმეტსახელები:")
#     for n in nicknames:
#         print(f"შენი ზედმეტსახელები: {n}")
# else:
#     print("არასწორი input! შეიყვანე მხოლოდ ერთი სიტყვა! (მხოლოდ ასობით)")




# 6. სორტირება
# მომხმარებელს შემოჰყავს რიცხვები თითო გამოტოვებით, (ულიმიტოდ რამდენიც უნდა) პროგრამა სთავაზობს
# როგორ უნდა რომ დაუსორტირდეს აღნიშნული: კლებადობით, ზრდადობით, random-ად, მხოლოდ
# უნიკალური მონაცემები დატოვოს. რომელსაც აირჩევს უნდა გამოვიდეს ზუსტად ისე დალაგებული სია.
#
# import random
#
# # მომხმარებლის input (space-ებით გაყოფილი რიცხვები)
# # წერს რიცხვებს ერთ ხაზზე (space-ებით გაყოფილად)
# numbers = list(map(int, input("შეიყვანე რიცხვები (space-ით): ").split()))
# # .split() → ყოფს ტექსტს space-ებით სიის სახით: ["5", "2", "9", ...]
# # map(int, ...) → თითოეულ string-ს აქცევს integer-ად
# # list(...) → საბოლოოდ ქმნის სრულ რიცხვების სიას
#
# print("\nაირჩიე სორტირების ტიპი:") # ვბეჭდავთ მენიუს სათაურს მომხმარებლისთვის
# print("1 - ზრდადობით")
# print("2 - კლებადობით")
# print("3 - random")
# print("4 - მხოლოდ უნიკალური მნიშვნელობები")
#
# you_choice = input("შენი არჩევანი: ")
#
# if you_choice == "1":
#     result = sorted(numbers) # sorted() აბრუნებს ახალ სიას, დალაგებულს ზრდადობით
# elif you_choice == "2":
#     result = sorted(numbers, reverse=True) # sorted(..., reverse=True) აბრუნებს დალაგებულ სიას კლებადობით
# elif you_choice == "3":
#     result = numbers[:] # numbers[:] ქმნის სიის ასლს, რათა ორიგინალი არ შეიცვალოს
#     random.shuffle(result) # shuffle შემთხვევითად არევს სიის ელემენტებს
# elif you_choice == "4":
#     # dict.fromkeys(numbers) შლის დუბლიკატებს და ინარჩუნებს რიგს
#     # შემდეგ list() აბრუნებს მას სიის ფორმატში
#     # უნიკალური ელემენტების შენარჩუნება (order preserved)
#     result = list(dict.fromkeys(numbers))
# else:
#     print("არასწორი არჩევანია!")
#     result = [] # ვაბრუნებთ ცარიელ სიას, რადგან valid შედეგი არ გვაქვს
# print("\nშედეგი:", result) # საბოლოო შედეგს ვბეჭდავთ




# 7. ტექსტის ფილტრი: მომხმარებელს შეყავს ტექსტი. ამოცანა: პროგრამამ უნდა
# წაშალოს ყველა ციფრი და სიმბოლო, დატოვოს მხოლოდ ასოები და სივრცეები.

# customer_text = input("შეიყვანეთ ნებისმიერი ტექსტი: ")
# result = ""
#
# # გადავივლით თითო სიმბოლოზე ტექსტში
# for char in customer_text:
#     # თუ სიმბოლო არის ასო ან სივრცეები ვტოვებთ
#     if char.isalpha() or char == " ":
#         result += char
#
# # საბოლოო შედეგი
# print("გაფილტრული ტექსტი:", result)




# 8. პირამიდა: მომხმარებელს შეყავს რიცხვების სია (მაგ. 3,5,7,2).
# ამოცანა: შექმენი “პირამიდა”, სადაც ყოველი ახალი რიგი ზემოთა წინა ორი რიცხვის ჯამია.
# 3  5  7  2
#  8  12  9
#   20  21
#     41

# მომხმარებელი წერს რიცხვებს space-ებით
customer_numb = list(map(int, input("შეიყვანეთ რიცხვები სფეისებით: ").split()))

# სანამ სიაში ერთზე მეტი ელემენტია
while len(customer_numb) > 1:
    # მიმდინარე რიგის დაბეჭდვა
    print(*customer_numb)

    # ახალი სიის შესაქმნელად
    new_row = []

    # მეზობელი ელემენტების ჯამი
    for i in range(len(customer_numb) - 1):
        new_row.append(customer_numb[i] + customer_numb[i + 1])

    # გადავდივართ ახალ რიგზე
    customer_numb = new_row

print(customer_numb)








