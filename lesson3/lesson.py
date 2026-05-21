from random import random
from datetime import datetime

# 1. გაქვთ ონლაინ მაღაზია, როდესაც მომხმარებელი შემოდის პროგრამის გაშვებისას უნდა
# გამოუჩნდეს მენიუ მაგალითად: “გამარჯობა” თქვენ იმყოფებით მაღაზია SpaceX-ში, პროდუქტები:
# რაკეტა - 15000$, ხომალდი - 25000$, ჩაფხუტი - 5000$ და ა.შ. მომხმარებელს უნდა ჰკითხოთ
# რომელი ნივთები უნდა და დაუთვალოთ რა დაუჯდება ჯამურად, თუ დაგეთანხმებათ უნდა მიჰყიდოთ
# ნივთები თუ უარს იტყვის შეთავაზებაზე უნდა დაასრულოთ მუშაობა.

# გვაქვს პროდუქტები და მათი ფასები
shop_items = {
    "რაკეტა": "15000$",
    "ხომალდი": "25000$",
    "ჩაფხუტი": "5000$"
}

# შევქმნათ სტრინგი სადაც იქნება პროდუქტები და მათი ფასები, რომ გამოვიტანოთ მომხმარებლისთვის
# შევკრიბე პროდუქტები და მათი ფასები ერთ სტრინგში, რომელიც შემდეგ გამოვიტანე
product = ""
shop_item_key_list = []
shop_item_value_list = []
for key, value in shop_items.items(): # ამოვიღებთ პროდუქტებს და ფასებს
    product += f"{key} - {value}, "
    shop_item_key_list.append(key)
    shop_item_value_list.append(value)

print(f"გამარჯობა, თქვენ იმყოფებით მაღაზია SpaceX-ში, პროდუქტები: {product}")

total = 0
start_shopping = True

while start_shopping:
    # მომხმარებელს ვეკითხებით რომელი ნივთები უნდა
    question_customer = input("რომელი ნივთი გნებავთ? (next - შეკვეთის დასრულება), (exit - მაღაზიიდან გასვლა): ")

    if question_customer == "exit":
        print(f"თქვენ გამოხდით მაღაზიიდან")
        start_shopping = False
        break

    if question_customer == "next":
        start_shopping = True
        break

    if question_customer in shop_item_key_list:
        find_index = shop_item_key_list.index(question_customer) # ლისტიდან ვიპოვოთ ინდექსი
        price = shop_item_value_list[find_index] # ლისტიდან მინიჭებული ფასი
        price = price[:-1] # ამოვიღებთ ფასიდან დოლარის ნიშანს, რომ შევძლოთ მიმატება
        total += int(price) # საბოლოო ფასი
        print(f"ჯამი: {total}")
    else:
        print("ასეთი ნივთი არ არსებობს, გთხოვთ სწორი დასახელება შეიყვანოთ")


# სანამ exit-ს დაწერს მომხმარებელი იქამდე ეს ლოგიკა იმუშავებს, თუ exit-ს დაწერს აქ არარ მოვა ლოგიკა
if question_customer != "exit":
    response_ok = "კი"
    response_fail = "არა"
    question_order = input(
        f"არჩეული ნივთების სრული ღირებულებაა: {total}, გნებავთ? შეიყვანეთ პასუხი {response_ok} ან {response_fail}"
    )

    if question_order == response_ok:
        print(f"გილოცავთ თქვენ შეიძინეთ წარმატებით!")
    elif question_order == response_fail:
        print(f"თქვენი შეკვეთა წარმატებით გაუქმდა!")
    elif question_order != response_ok and question_order != response_fail:
        input(f"არჩეული ნივთების სრული ღირებულებაა: {total}, გნებავთ?")
        if question_order == response_ok:
            print(f"გილოცავთ თქვენ შეიძინეთ წარმატებით!")
        elif question_order == response_fail:
            print(f"თქვენი შეკვეთა წარმატებით გაუქმდა!")
    else:
        print(f"არასწორია პასუხი, თავიდან სცადეთ!")





# 2. While loop და FOR LOOP-ის გამოყენებით დაწერეთ ციკლი, რომელიც დაბეჭდავისას, გვერდით
# დაუწერს რიცხვს ლუწია თუ კენტი 20-მდე. (დაწერეთ ორივე ვარიანტი)

x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
i = 0

while i < len(x):
    if x[i] == 0:
        print(f"{x[i]} zero")
        i += 1
    if x[i] % 2 == 0:
        print(x[i], "even")
        i += 1
    else:
        print(x[i], "odd")
        i += 1


for i in x:
    if i == 0:
        continue
    elif i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")






# 3. გამოითვალეთ თითოეული სტუდენტის საშუალო არითმეტიკული ქულა და დააბრუნეთ მისთვის
# შესაფერისი ნიშანი:
students = {
    "Ana": [89,66,12,75,11],
    "Giorgi": [67,72,90,91,55],
    "Levant": [49,36,88,98,34],
    "Veronika": [99,88,32,65,99],
    "Nika": [77,81,41,73,99]
}
print(students)


for key, value in students.items():
    average = sum(value) / len(value)
    # print(f"{key}, {sum(value)}")
    print(f"{key}, {average} ქულა")






# 4. დაწერეთ ციკლი, რომელიც მოითხოვს მომხმარებლისგან ასაკის შეყვანას, თუ შეყვანილი
# მონაცემი არ იქნება რიცხვური ტიპის, მაშინ ციკლი დატრიალდეს და თავიდან კითხოს, სხვაგვარად
# დაუანგარიშოს დაბადების თარიღი.

age = input("გთხოვთ შეიყვანოთ ასაკი")
current_year = datetime.now().year
# print(current_year)

while age:
    if age.isdigit():
        age = int(age)
        birth_year = current_year - int(age)
        print(f"თქვენი დაბადების წელია: {birth_year}")
        break
    else:
        age = input("გთხოვთ შეიყვანოთ ასაკი")





# 5. While ციკლის მეშვეობით დაითვალეთ მოცემული მასივის:
# mylist = range(100)
# *მეორე ხარისხი
# *მესამე ხარისხი

mylist = range(100)
i = 0
two = 0
three = 0

while i < len(mylist):
    two = 0 # უნდა განულდეს ლუპში რადგან ყოველი იტერაციის დროს მიღებულ რიცხვს არ დაუმატოს ახალი რიცხვი კვადრატში
    two += (mylist[i] ** 2)

    three = 0 # უნდა განულდეს ლუპში რადგან ყოველი იტერაციის დროს მიღებულ რიცხვს არ დაუმატოს ახალი რიცხვი კუბში
    three += (mylist[i] ** 3)

    i += 1

    print(f"მეორე ხარისხად: {two}, მესამე ხარისხად: {three}, იტერაცია: {i}")

    if i == 99:
        break

print(f"მეორე ხარისხად: {two}, მესამე ხარისხად: {three}, საბოლოოდ იტერაცია: {i}")





# 6. FOR ციკლის/ციკლების გამოყენებით შექმენი გამრავლების ტაბულა და ტერმინალში გამოიტანე
# მსგავსი ფორმატით:
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30
# 4 8 12 16 20 24 28 32 36 40
# 5 10 15 20 25 30 35 40 45 50
# 6 12 18 24 30 36 42 48 54 60
# 7 14 21 28 35 42 49 56 63 70
# 8 16 24 32 40 48 56 64 72 80
# 9 18 27 36 45 54 63 72 81 90
# 10 20 30 40 50 60 70 80 90 100

for i in range(1,11):
    for j in range(1,11):
        print(i*j)

"""
როცა i არის 1, იგი მრავლდება j-ზე სანამ j არ ამოიწურება 1-დან 10-ის ჩათვლით,
შემდეგ i არის 2 და მრავლდება ისევ j-ზე 1-დან 10-ის ჩათვლით, ასე გრძელდება
მანამ სანამ არ მივა i 10-ზე. საბოლოოდ i 10-ზე გამრავლდება j 10-ზე (10*10=100)
და დასრულდება ლუპის მუშაობა.

"""





# 7. გააანალიზე კოდის ფრაგმენტი და შემდეგ გაასწორე შეცდომები, ასევე დაწერე ახსნა:
# numbers = ["1", "2", "3", "4"]
# total = 0
# for n in numbers:
# total += n
# print("Total:", total)


numbers = ["1", "2", "3", "4"]
total = 0

for n in numbers:
    total += int(n)

print(f"Total: {total}")

"""
# სინტაქსი უნდა იყოს სწორი პირველ რიგში for-ის შიგნით უნდა იყოს total
# გვაქვს string-ების ლისტი და ვერ მივუმატებთ ერთმანეთს total-ს (int) და n-ს (str)
# n-ს გადავკასტავთ int-ში
# print-ი უნდა იყოს გარეთ რადგან დავბეჭდოთ სრული და არა ლუპის ყველა იტერაციაზე
# print-ში კარგია თუ f სტრინგ დავწერთ, რომ უფრო გასაგები იყოს

"""





# 8. გამოიყენე FOR ციკლი რომელიც მიწვდება data ყველა ელემენტს და დაწერე შემდეგი ლოგიკა, თუ ელემენტი არის სტრინგი
# და შეიცავს მხოლოდ რიცხვს გადააქციე რიცხვად და შეინახე total-ში, თუ რიცხვია პირდაპირ შეინახე total-ში, თუ სხვა
# ტიპის მონაცემთა ტიპია გამოტოვე. ბოლოს დაბეჭდე სრული ჯამი.
data = ["5", 0, "3", True, "", 2, "x", False]
total = 0

for x in data:
    if type(x) == str and x.isdigit():
        total += int(x)
    elif type(x) == int:
        total += x
    else:
        continue

print(f"total: {total}") # დაიბეჭდება უკვე ციკლის გარეთ სრულად total





# 9. დაწერეთ FOR LOOP სადაც მიწვდებით მონაცემებს, თუ მნიშვნელობა არის სტრინგი და შეიცავს
# მხოლოდ რიცხვს გამოიყენე კასტინგი და შეინახე, თუ ინთეჯერია შეინახე პირდაპირ, თუ ბულიენია
# გადააქციე და შეინახე (მხოლოდ True) სხვა ყველა ტიპის მონაცემი გამოტოვე.

transactions = {
    "გიო": "100",
    "ნიკა": 50,
    "აკაკი": "30a",
    "ლევანი": 0,
    "ანა": "70",
    "მარი": True
}
total = 0

for key, value in transactions.items(): # დაიბეჭდება key და value წყვილები
    print(f"{key}: {value}")

    if type(value) == str and value.isdigit():
        total += int(value)
    elif type(value) == int:
        total += value
    elif type(value) == bool and value == True:
        total += int(value)
    else:
        continue

print(f"total: {total}") # დაიბეჭდება უკვე ციკლის გარეთ სრულად total





# 10. შექმენი პროგრამა (თამაში) სადაც მომხმარებელი შეძლებს გამოიცნოს შენი ჩაწერილი რიცხვი,
# მომხმარებელი წერს ციფრებს და ცდილობს გამოიცნოს შენი რიცხვი, დიაპაზონი 0-დან 51-მდე, თუ
# მომხმარებელმა ჩაწერა ამ დიაპაზონს გარეთ უნდა გამოუტანო შეტყობინება რომ “რიცხვი სცდება
# არეალს”, თუ ჩაწერა “exit” გამორთე თამაში, უნდა დაუთვალო მცდელობების რაოდენობა და
# გამოიტანო შეტყობინება: “გილოცავ გამოიცანი XX რიცხვი, მცდელობა: XX”

customer_response = input(f"შეიყვანეთ რიცხვი 0-დან 50-ის ჩათვლით: ")
random_numbers = int(random() * 51)
game_start = True
customer_try = 0

while game_start:
    if customer_response == "exit":
        game_start = False
        break
    else:
        if customer_response.isdigit():
            customer_response = int(customer_response)
            if customer_response > 50 or customer_response < 0:
                customer_try += 1
                print("რიცხვი სცდება არეალს")
                customer_response = input(f"შეიყვანეთ რიცხვი 0-დან 50-ის ჩათვლით")
            elif 0 <= customer_response <= 50 and customer_response != random_numbers:
                customer_try += 1
                print("რიცხვი არეალშია, მაგრამ არასწორია!")
                customer_response = input(f"შეიყვანეთ რიცხვი 0-დან 50-ის ჩათვლით")
            elif customer_response == random_numbers:
                print(f"გილოცავ გამოიცანი {random_numbers} რიცხვი, მცდელობა {customer_try}")
                game_start = False
            else:
                print("რაღაც შეცდომაა!")
        else:
            customer_response = input(f"შეიყვანეთ მხოლოდ რიცხვი! 0-დან 50-ის ჩათვლით")
