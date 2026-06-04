# 1. შექმენი გენერატორი, რომელიც ტექსტის თითოეულ სიმბოლოს აბრუნებს.
# word = "CODE"
# def symb_each_gen(word):
#     for i in word:
#         yield i
#
# symb_each_gen(word)
# gen = symb_each_gen(word)
# for symbol in gen:
#     print(symbol)



# 2. დაწერე პროგრამა რომელშიც მომხმარებელი შემოიყვანს მხოლოდ ციფრებს, ლოგიკა უნდა იყოს შემდეგი: გვაქვს კონკრეტული ლისტი და
# მომხმარებელი უნდა მიწვდეს შემოყვანილი ციფრით რომელიმე ელემენტს, თუ ვერ მიწვდება პროგრამა შეცდომაზე არ უნდა გავიდეს.
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# customer_inp = input("შემოიყვანეთ ციფრი")
#
# def numb_list_check(arr):
#     try:
#         if customer_inp.isdigit() and int(customer_inp) in arr:
#             print(f"გილოცავ გამოიცანი!")
#     except TypeError as t:
#         print(f"შეიყვანეთ მხოლოდ ციფრები! {t}")
#     except ValueError as v:
#         print(f"შეიყვანეთ მხოლოდ ციფრები! {v}")
#     except Exception as e:
#         print(f"გაუთვალისწინებელი შეცდომა! {e}")
#     finally:
#         print(f"პროგრამა შესრულდა, ლისტში ციფრებია: {arr}")
#
# numb_list_check(arr)



# 3. შექმენი დეკორატორი, რომელიც ითვლის რამდენჯერ გამოიძახეს ფუნქცია. მაგალითი:
# @counter
# def say():
# print("Hi")
# say()
# say()
# გამოძახება: 1
# Hi
# გამოძახება: 2
# Hi

# def counter(func):
#     count = 0
#
#     def wrapper(*args,**kwargs):
#         nonlocal count # ეუბნება Python-ს: ეს count არ არის ლოკალური ცვლადი, აიღე ის გარე ფუნქციიდან.
#         count += 1
#         print(f"გამოძახება: {count}")
#         return func(*args,**kwargs)
#     return wrapper
#
# @counter
# def say():
#     print("Hi")
#
# say()
# say()
# say()
# say()

# მეხსიერების წესი (Scope). Python ცვლადებს ეძებს ამ თანმიმდევრობით:

# Local — მიმდინარე ფუნქცია
# Enclosing — გარე ფუნქცია (nonlocal)
# Global — ფაილის დონე (global)
# Built-in — print, len, range და ა.შ.

# ამ წესს ხშირად LEGB Rule ეწოდება



# 4. მომხმარებელს უნდა დავუსვათ 5 მათემატიკური შეკითხვა, თითოეულზე სწორი პასუხი არის 10 ქულა,
# ხოლო არასწორი 0 ქულა, მიღებული პასუხებიდან უნდა განვსაზღვროთ რამდენი ქულა აიღო მომხმარებელმა,
# შევქმნათ ლოგ ფაილი game.log და შევინახოთ ყველა ქულა. ბოლოს გამოვუტანოთ მიღებული შედეგი.

# quest1 = input(f"რამდენია 3+2: ")
# quest2 = input(f"რამდენია 3-2: ")
# quest3 = input(f"რამდენია 3*2: ")
# quest4 = input(f"რამდენია 2/2: ")
# quest5 = input(f"რამდენია 12%2*2: ")
#
# score = 0
#
# if quest1 == "5":
#     score += 10
# if quest2 == "1":
#     score += 10
# if quest3 == "6":
#     score += 10
# if quest4 == "1":
#     score += 10
# if quest5 == "3":
#     score += 10
#
# with open("game.log", "a", encoding="utf-8") as file:
#     file.write(f"მომხმარებლის ქულა {score}\n")
#
# print(f"თქვენ დააგროვეთ {score} ქულა 50-დან")



# 5. შექმენით ფაილი quiz.log, შექმენით გენერატორი რომელშიც შენახული იქნება 5 შეკითხვა და სათითაოდ დააბრუნებს,
# მომხმარებელმა უნდა უპასუხოს ყველა შეკითხვას და პასუხები შეინახეთ ლოგ ფაილში.

# def quiz_gen():
#     quest = (
#         "რამდენია 2+2?",
#         "რამდენია 5-3?",
#         "რამდენია 3*3?",
#         "რამდენია 10/2?",
#         "რამდენია 12%5?"
#     )
#
#     for q in quest:
#         yield q
#
# gen = quiz_gen()
#
# # "r" - read,
# # "w" - write,
# # "a" - append,
# # "x" - eXclusive Create,
# # "r+" - read + write - წაკითხვა და ჩაწერა,
# # "w+" - read + write - თუმცა ჯერ ასუფთავებს ფაილს,
# # "a+" - read + add - წაკითხვა და ბოლოში დამატება
#
# with open("quiz.log", "a", encoding="utf-8") as file:
#     for question in gen:
#         answer = input(question + " ")
#         file.write(f"{question} -> {answer}\n")



# 6. შექმენი პროგრამა სადაც მომხმარებელი ეჯიბრება კომპიუტერს: ქვა/ბადე/მაკრატელის თამაშში, თამაში არის სამამდე, კომპიუტერი
# შემთხვევითობის პრინციპით ირჩევს ამ სამიდან 1-ს, ასევე ტერმინალში მომხმარებელი წერს ერთერთს, ერთნაირის შემთხვევაში ფრეა
# და გრძელდება თამაში 3-მდე, ვინც პირველი მიაღწევს 3-ს გამოიტანე შეტყობინება …..-მ გაიმარჯვა, ყველა ნათამაშები ხელი უნდა
# შეინახოო ლოგირების ფაილში.

# import random, logging
#
# logging.basicConfig(
#     filename="customerVScomputer.log",
#     level=logging.DEBUG,
#     encoding="utf-8",
#     format="%(asctime)s - %(message)s"
# )
#
# choices = ["ქვა", "ბადე", "მაკრატელი"]
# player_score = 0
# computer_score = 0
#
# with open("customerVScomputer.log", "a", encoding="utf-8") as file:
#     logging.debug(f"თამაში დაიწყო\n\n")
#
#     while player_score < 3 and computer_score < 3:
#
#         player_choice = input("აირჩიე (ქვა/ბადე/მაკრატელი): ").lower()
#         computer_choice = random.choice(choices).lower()
#
#         logging.info(f"მომხმარებელი: {player_choice} | კომპიუტერი: {computer_choice}\n")
#         print(f"კომპიუტერმა აირჩია: {computer_choice}")
#
#         if player_choice == computer_choice:
#             print(f"ფრეა!")
#             continue
#         elif (
#             (player_choice == "ქვა" and computer_choice == "მაკრატელი")
#             or (player_choice == "მაკრატელი" and computer_choice == "ბადე")
#             or (player_choice == "ბადე" and computer_choice == "ქვა")
#         ):
#             player_score += 1
#             logging.info("რაუნდი მოიგე!")
#             print("რაუნდი მოიგე!")
#         else:
#             computer_score += 1
#             logging.warning("რაუნდი მოიგო კომპიუტერმა! უკეთესად თამაში გმართებთ!")
#             print("რაუნდი მოიგო კომპიუტერმა!")
#
#         print(f"ქულები -> მომხმარებელი: {player_score} | კომპიუტერი: {computer_score}")
#
#     if player_score == 3:
#         print("მომხმარებელმა გაიმარჯვა!")
#         logging.info("გამარჯვებული: მომხმარებელი\n\n")
#
#     else:
#         print("კომპიუტერმა გაიმარჯვა!")
#         logging.info("გამარჯვებული: კომპიუტერი\n\n")
#
#     logging.debug(f"თამაში დასრულდა!")



# 7. პროგრამა კამათელზე - გვყავს ორი მომხმარებელი Gamer 1 & Gamer 2, თითოეულს უნდა გავაგორებინოთ კამათელი თითო თითოჯერ,
# თუ ფრეა ვიმეორებთ, სხვა შემთხვევაში მოგებულ მოთამაშეს უნდა ვკითხოთ კიდევ 1 შანსს მისცემს თუ არა წაგებულს და კიდევ გააგორებს
# თუ არა, თუ უარია ვამთავრებთ, თუ თანახმაა იგივე ლოგიკა უნდა გაგრძელდეს სანამ უარს არ იტყვის ერთ-ერთი.





#8. შექმენი პროგრამა სადაც გექნება გადაცემული 10 სიტყვა ლისტში და ლოგიკა არის შემდეგი, ამ სიტყვებიდან 2 ცალს ირჩევ შემთხვევითობის
# პრინციპით და თითოეული სიტყვიდან უნდა ამოაკლო 2 ასო და მომხმარებელს აჩვენო მსგავსი ფორმით და უთხრა რომ გამოიცნოს სიტყვა და
# ჩაწეროს სრულად, თუ გამოიცნო “გამარჯვება” თუ ვერ გამოიცნო ვერცერთი სიტყვა “დამარცხდი”, ერთის გამოცნობის შემთხვევაში “50%”


