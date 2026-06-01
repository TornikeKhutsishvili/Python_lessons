# 1. მოცემულია სიტყვა "ABCD". დაბეჭდე ყველა შესაძლო ვარიანტი და **დაითვალე** რამდენია
# სულ რაოდენობრივად (უნდა დააბრუნო რიცხვი)  ->  word = "ABCD"

# def variants(word, quantity=""):
#     if len(word) == 0:
#         return 1
#
#     count = 0
#
#     for w in range(len(word)):
#         symbol = word[w]
#
#         # დარჩენილი სიტყვა
#         rest = word[:w] + word[w+1:]
#
#         # რეკურსია გამოვიყენე - ანუ ფუნქციის გამოძახება ფუნქციაში
#         count += variants(rest, quantity + symbol)
#
#     return count
#
# word = "ABCD"
# total = variants(word)
# print(f"Total: {total} variants")




# 2. იპოვე მომდევნო კვირის პირველი სამშაბათი, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)

# timedelta არის datetime კლასი, რომელიც წარმოადგენს დროის ინტერვალს (განსხვავებას).

# from datetime import date, timedelta
#
# dt = date.today()
# next_week_day = dt.isocalendar().weekday

# Monday = 1; Tuesday = 2; Wednesday = 3;
# Thursday = 4; Friday = 5; Saturday = 6; Sunday = 7;

# if next_week_day == 1:  # Monday
#     next_tuesday = dt + timedelta(days=8) # დღეს თუ ორშაბათია მაშინ მომდევნო კვირის სამშაბათამდე არის 7+1 დღე =8.
# elif next_week_day == 2:  # Tuesday
#     next_tuesday = dt + timedelta(days=7) # დღეს თუ ორშაბათია მაშინ მომდევნო კვირის სამშაბათამდე არის 6+1 დღე =7.
# elif next_week_day == 3:  # Wednesday
#     next_tuesday = dt + timedelta(days=6) # ...
# elif next_week_day == 4:  # Thursday
#     next_tuesday = dt + timedelta(days=5) # ...
# elif next_week_day == 5:  # Friday
#     next_tuesday = dt + timedelta(days=4) # ...
# elif next_week_day == 6:  # Saturday
#     next_tuesday = dt + timedelta(days=3) # ...
# else:  # Sunday
#     next_tuesday = dt + timedelta(days=2) # ...
#
# print(f"შემდეგი კვირის პირველი სამშაბათი არის: {next_tuesday}")




# 3. დაადგინე, არის თუ არა შეყვანილი წელი ნაკიანი, მომხმარებელს შემოჰყავს მხოლოდ წელი და ვეუბნებით არის თუ არა ნაკიანი

# import calendar
# #
# # from lesson3.lesson import data
# #
# # myinput = int(input("შეიყვანეთ წელი და გაიგეთ ნაკიანია თუ არა"))
# #
# # is_leap = calendar.isleap(myinput)
# # # isleap return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# #
# # if is_leap:
# #     print("ნაკიანი წელიწადია")
# # else:
# #     print("არ არის ნაკიანი წელიწადი")


# 4. დაითვალე რამდენი კვირაა დარჩენილი ახალ წლამდე, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)

# from datetime import date, timedelta
#
# today = date.today()
# next_year = today.year + 1
# new_year = date(next_year, 1, 1)
# difference = new_year - today
# days_left = difference.days
# weeks_left = days_left / 7
#
# print(f"{weeks_left:.2f} კვირა დარჩა ახალ წლამდე")




# 5. შექმენი ყველა 3-ელემენტიანი კომბინაცია სიიდან \[1,2,3,4,5] (itertools-ის გამოყენებით)

# import itertools
# my_list = [1,2,3,4,5]
# counter = 0
#
# for i in itertools.permutations(my_list, 3):
#     counter += 1
#     print(i)
#
# print(counter)




# 6. მიიღე ყველა კომბინაცია "XYZ"-ის სიმბოლოებით სიგრძე 1-დან 3-მდე
# მაგალითი: X, Y, Z, XY, XZ, YZ, XYZ უნდა მივიღოთ მსგავსი შედეგი.

# permutations - რიგითობასაც მიუყვება, ხოლო combinations-ია უბრალოდ კონკრეტული ჯგუფების კომბინაციებს

# import itertools
#
# my_str = "XYZ"
# my_str_result = ""
#
# for iter_str in range(1, len(my_str) + 1): # ვცვლით კომბინაციის სიგრძეს: 1-დან სტრინგის სიგრძემდე (3-მდე)
#     for combination in itertools.combinations(my_str, iter_str): # ვქმნით კომბინაციებს მოცემული სიგრძით
#         print(my_str_result.join(combination)) # tuple-ს ვაქცევთ სტრინგად და ვბეჭდავთ




# 7. თამაში უკუსვლაზე

# კომპიუტერი ირჩევს შემთხვევითობის პრინციპით რიცხვს 1-20 მდე, მოთამაშეს აქვს მხოლოდ 5 წამი რიცხვის გამოსაცნობად,
# თუ 5 წამში სწორ რიცხვს ვერ შეიყვანს, თამაში სრულდება და გამოდის ტექსტი "დრო ამოიწურა, თქვენ დამარცხდით".

# from datetime import datetime, timedelta
# import time, random
#
# comp_choice = random.randint(1,20)
# start_time = datetime.now()
# time_limit = timedelta(seconds=5)
#
# customer_numb = input("შეიყვანეთ სასურველი რიცხვი (1-20), დრო: 5 წამი!")
#
# end_time = datetime.now()
# finish_time = end_time - start_time
#
# # print("კომპიუტერის რიცხვი:", comp_choice)
#
# if finish_time > time_limit:
#     print("დრო ამოიწურა, თქვენ დამარცხდით!")
# else:
#     if int(customer_numb) == comp_choice:
#         print("სწორია, თქვენ მოიგეთ!")
#     else:
#         print("არასწორია, თქვენ დამარცხდით!")




# 8. ორი მოთამაშე იწყებს "გარბენს". უნდა შეამოწმო რომელი დაასრულებს ნაკლებ დროში

# from datetime import datetime, timedelta
# import random
#
# start = datetime.now()
#
# random_time1 = random.randint(5,20)
# random_time2 = random.randint(5,20)
#
# player1 = start + timedelta(seconds=random_time1)
# player2 = start + timedelta(seconds=random_time2)
#
# print(f"Player 1: {player1}")
# print(f"Player 2: {player2}")
#
# if player1 > player2:
#     print(f"ნაკლებ დროში დაასრულა მეორე მოთამაშემ - {player2}")
# elif player1 < player2:
#     print(f"ნაკლებ დროში დაასრულა პირვემა მოთამაშემ - {player1}")
# elif player1 == player2:
#     print(f"თანაბარ დროში დაასრულა ორივე მოთამაშემ")
# else:
#     print("დაფიქსირდა ხარვეზი!")




# 9. იღბლიანი დაბადების დღე
# მოთამაშემ უნდა შეიყვანოს დაბადების თარიღი და თამაში დაითვლის რამდენი დღეა დარჩენილი შემდეგ დაბადების დღემდე
# birthday = date(2000, 12, 10)

# from datetime import date
#
# tday = date.today()
#
# player_birth_inp = input("შეიყვანეთ დაბადების თარიღი, ფორმატი: (წელი:თვე:დღე) ")
#
# # დაშლა ცვლადებად (year, month, day)
# # ტექსტიდან რიცხვების მიღება: map(int, split())
# year, month, day = map(int, player_birth_inp.split(":"))
#
# birthday = date(year, month, day) # დაბადების თარიღი (საბაზო)
# next_birthday = date(tday.year, month, day) # ამ წლის დაბადების დღე
#
# # თუ უკვე გავიდა ამ წლის დაბადების დღე, მაშინ გადავდივართ შემდეგ წელზე
# if next_birthday < tday:
#     next_birthday = date(tday.year + 1, month, day)
#
# # სხვაობა დღეებში
# days_left = (next_birthday - tday).days
#
# print("დღეები შემდეგ დაბადების დღემდე:", days_left)




# 10. საცავი - ჯუნიორ ჰაკერი :)

# თამაში არის შემდეგი - გვაქვს სეიფი რომელსაც აქვს ციფრები 1-6 მდე პაროლი არ ვიცით, ყოველ დღე
# კომპიუტერი აგენერირებს ახალ პაროლს (შემთხვევითობის პრინციპით) პაროლი არის 4 ციფრიანი. ჩვენი
# მიზანია დავწეროთ ისეთი კოდი რომელიც შეამოწმებს ვარიანტებს და როცა მოხდება კომპიუტერის მიერ
# დაგენერირებული პაროლის დამთხვევა უნდა გამოვიტანოთ შეტყობინება "პაროლი სწორია, საცავი გახსნილია",
# აუცილებელი პირობაა გამოვიტანოთ ყველა ჩვენს მიერ ნაცადი პაროლი სანამ მივალთ სწორ ვარიანტამდე.

import itertools, random

counter = 0
password = tuple(random.randint(1, 6) for _ in range(4))
# print(f"გენერირებული პაროლი:, {password}")

# product() გამოვიყენეთ, რადგან პაროლში ციფრები შეიძლება განმეორდეს.
for guess in itertools.product(range(1, 7), repeat=4):
    counter += 1
    print(f"ნაცადი პაროლი {guess}")

    if guess == password:
        print("პაროლი სწორია, საცავი გახსნილია!")
        break
print(f"{counter} ცდა")
