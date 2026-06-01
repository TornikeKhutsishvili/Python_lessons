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
