# 1. შეინახეთ ცვლადებში ცვლადების ტიპები მათი მნიშვნელობების ნაცვლად
# var1 = 1
# var2 = -1
# var3 = True
# print(var1, var2, var3)

var1 = int
var2 = int
var3 = bool
print(var1, var2, var3)




# 2. შეცვალეთ ცვლადების ტიპები (type casting-ის მეშვეობით)
# var4 = False # გადაიყვანეთ Float -ში
# var5 = 3 # გადაიყვანეთ Float -ში
# var6 = {"key":"value", "key1":"value", "key3":"value"} # გადაიყვანეთ list -ში
# print(var4, var5, var6)

var4 = float(False) # გადაიყვანეთ Float -ში
var5 = float(3) # გადაიყვანეთ Float -ში
var6 = [{"key":"value", "key1":"value", "key3":"value"}] # გადაიყვანეთ list -ში

print(var4, var5, var6)




# 3. შექმენით შესაფერისი ტიპის ცვლადები მონაცემებისთვის.
# group:
# name: Python2023
# count: 35
# male: 22
# female: 13
# students: Student1, Student2, Student3, Student4, Student5
# ages: 24,33,15,45,42

group = {
    "name": "Python2023",
    "count": int(35),
    "male": int(22),
    "female": int(13),
    "students": ["Student1", "Student2", "Student3", "Student4", "Student5"],
    "ages": [24, 33, 15, 45, 42],
}




# 4. დააფორმატეთ სტრიქონი და გამოითვალეთ თქვენი ასაკი
birth_year = 2001 # ჩაწერეთ წელი
name = "თორნიკე" # ჩაწერეთ სახელი
surname = "ხუციშვილი" # ჩაწერე გვარი
current_year = 2026
# უნდა მიიღოთ შემდეგი წინადადება - მე ‘სახელი’ ‘გვარი’ დავიბადე ‘ამ წელს’ შესაბამისად ვარ
# ‘ამდენი წლის’

bio = f"მე {name} {surname} დავიბადე {birth_year} წელს, შესაბამისად ვარ {current_year}-{birth_year} წლის"
print(bio)




# 5. გამოითვალეთ მომხრეთა და მოწინააღმდეგეთა პროცენტი და აჩვენეთ ორივე.
# (შეეცადეთ დაამრგვალოთ პროცენტები მეასედებამდე)
# მაგალითი:
# YES: 1234 = 34.80%
# NO: 2312 = 65.20%

Yes = 119
No = 82

total_votes = Yes + No
yes_percentage = round((Yes / total_votes) * 100)
no_percentage = round((No / total_votes) * 100)
print(f"YES: {Yes} = {yes_percentage:}%")
print(f"NO: {No} = {no_percentage:}%")




# 6. გადაიყვანეთ 3670 წამი საათებად და წუთებად
seconds = 3670
# დაბეჭდეთ: "X საათი Y წუთი Z წამი"

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds -= ((hours * 3600) + (minutes * 60))

print(f"{hours} საათი  {minutes} წუთი  {seconds} წამი")




# 7. გამოიტანეთ სტრიქონის პირველი და ბოლო ასო
text = "Python"

first = text[0]
last = text[-1]
print(f"{first} {last}")




# 8. გამოითვალეთ სასწავლო საგნის შეფასების პროცენტული წილი
math = 45
total = 60
# დაბეჭდეთ: "პროცენტი: XX%"

point = round((math/total) * 100)
print(f"{point}%")




# 9. გამოითვალეთ ასაკი მომავალ წელს
birth_year = 2000
current_year = 2026
# დაბეჭდეთ ფორმატში:
# “მომავალ წელს შენ იქნები XX წლის”

age = current_year - birth_year + 1
print(f"მომავალ წელს შენ იქნები {age} წლის")




# 10. 350 წუთი რამდენი საათია და რამდენი წუთი დარჩება გამოიტანეთ
minutes = 350
# მაგალითი: “X საათი და XX წუთი”

hours = minutes // 60
minutes -= hours * 60
print(f"{hours} საათი და {minutes} წუთი")