# imports
import random
from enum import Enum
from abc import ABC, abstractmethod
from itertools import combinations


# 1. ლაბირინთი
# გვაქვს მოცემული მსგავსი ლაბირინთი:
# maze = [
# ["S", ".", "#", ".", "."],
# ["#", ".", "#", ".", "#"],
# [".", ".", ".", ".", "."],
# ["#", "#", "#", ".", "#"],
# [".", ".", ".", ".", "E"]
# ]

# S -> არის საწყისი წერტილი
# E -> არის საბოლოო წერტილი
# # -> არის კედელი
# . -> არის გზა, რომელიც უნდა გაიაროს მომხმარებელმა. თქვენი მიზანია დაწეროთ ლოგიკა სადაც მომხმარებელს შეეკითხებით რომელ
# მხარეს უნდა წასვლა: მაღლა, დაბლა, მარცხნივ, მარჯვნივ. თუ სწორად აირჩევს უნდა უთხრა რომ სწორად მიდის და კიდევ ჰკითხო
# ახლა რომელ მხარეს უნდა წასვლა, არასწორი გზის არჩევის შემთხვევაში უნდა დააწყებინო თავიდან თამაში და ისევ ჰკითხო სად წავა,
# თუ გავა ბოლოში უნდა დაუწერო რომ “შენ გაიარე ლაბირინთი” ვალიდაცია არაა საჭირო მომხმარებელს სწორად შეჰყავს სიტყვები.

class Directions(Enum):
    TOP = "მაღლა"
    BOTTOM = "დაბლა"
    LEFT = "მარცხნივ"
    RIGHT = "მარჯვნივ"

class RoadGame():
    def __init__(self):
        self.maze = [
            ["S", ".", "#", ".", "."],
            ["#", ".", "#", ".", "#"],
            [".", ".", ".", ".", "."],
            ["#", "#", "#", ".", "#"],
            [".", ".", ".", ".", "E"]
        ]
        self.start_row = 0
        self.start_col = 0

        self.current_row = self.start_row
        self.current_col = self.start_col

    def move(self, direction):
        new_row = self.current_row
        new_col = self.current_col

        if direction == Directions.TOP:
            self.new_col -= 1
        elif direction == Directions.BOTTOM:
            self.new_col += 1
        elif direction == Directions.LEFT:
            self.new_row -= 1
        elif direction == Directions.RIGHT:
            self.new_row += 1
        else:
            print("Invalid direction.")

        if (new_row < 0 or new_row >= len(self.maze) or new_row < 0 or new_row >= len(self.maze[0])):
            self.reset_game()
            return False

        if self.maze[self.current_row][self.current_col] != "#":
            self.reset_game()
            return False

        self.current_row = new_row
        self.current_col = new_col

        print("სწორად მიდიხარ!")
        return True

    def is_finished(self):
        return self.maze[self.current_row][self.current_col] == "E"

    def play(self):
        print("ლაბირინთი დაიწყო!")

        while True:
            direction = input("\nაირჩიე მიმართულება (მაღლა, დაბლა, მარცხნივ, მარჯვნივ): ")
            self.move(direction)
            if self.is_finished():
                print("\nშენ გაიარე ლაბირინთი!")
                break

    def reset(self):
        self.current_row = self.start_row
        self.current_col = self.start_col
        print("\nარასწორი გზა! თამაში თავიდან დაიწყო.\n")

maze_game = RoadGame()
maze_game.play()



# 2. თამაში 1 VS 1:
# თქვენი მიზანია შექმნათ თამაში სადაც ორი ადამიანი ეჯიბრება ერთმანეთს, მომხმარებელს უნდა ჰქონდეს 5-დან 1 მებრძოლის არჩევა:
# “გიგანტი”, “სწრაფი”, “მოქნილი”, “აქილევსი” & “პითონისტი”, თითოეულს გაუკეთეთ 3 შესაძლებლობა იგივე skill მაგალითად:
# ცეცხლის სროლა, ყინულის და ა.შ. სიცოცხლეები განსხვავებული უნდა ჰქონდეთ და ასევე დარტყმის ძალებიც. ჯერ პირველი მოთამაშეს
# ვარჩევინებთ გმირს, შემდეგ მეორეს (ერთნაირის არჩევა შეუძლიათ), მერე იწყებს პირველი მოთამაშე და ირჩევს ამ გმირზე რა სკილებიცაა
# იქიდან ერთს და ესვრის მეორეს, ასევე აკეთებს მეორე მოთამაშეც, ყოველ სროლაზე უნდა გამოუტანო დარჩენილი სიცოცხლე მოთამაშეს.

class Fighter:
    def __init__(self, name: str, hp: int, base_power: int, skills: dict):
        self.name = name
        self.hp = hp
        self.base_power = base_power
        # skills = {"skill_name": damage_multiplier}
        self.skills = skills

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def attack(self, target: "Fighter", skill_name: str):
        multiplier = self.skills[skill_name]
        damage = int(self.base_power * multiplier)
        target.take_damage(damage)
        print(f"\n{self.name}-მა გამოიყენა '{skill_name}' და მიაყენა {damage} დარტყმა!")
        print(f"{target.name}-ს დარჩენილი სიცოცხლე: {target.hp}")


# ------ 5 გმირის "ბანკი" (template-ები) -------
# ყველას აქვს თავისი 3 უნიკალური skill, განსხვავებული hp და power

ROSTER = {
    "გიგანტი": {
        "hp": 150,
        "power": 25,
        "skills": {
            "ცეცხლის სროლა": 1.5,
            "ქვის დარტყმა": 1.0,
            "ხტუნვა-დაჯაყვა": 2.0
        },
    },
    "სწრაფი": {
        "hp": 90,
        "power": 18,
        "skills": {
            "ცეცხლის სროლა": 1.2,
            "სატელ ჩარდახი": 1.8,
            "ელვისებური დარტყმა": 2.2
        },
    },
    "მოქნილი": {
        "hp": 100,
        "power": 20,
        "skills": {
            "ცეცხლის სროლა": 1.3,
            "ყინულის ისარი": 1.6,
            "ჩახუტება-გრიხვა": 1.9
        },
    },
    "აქილევსი": {
        "hp": 120,
        "power": 30,
        "skills": {
            "ცეცხლის სროლა": 1.4,
            "ხმლის დარტყმა": 2.5,
            "ფარით დაჯაყვა": 1.1
        },
    },
    "პითონისტი": {
        "hp": 80,
        "power": 22,
        "skills": {
            "ცეცხლის სროლა": 1.6,
            "კოდის წყევლა": 2.0,
            "ბაგ-ექსპლოიტი": 1.7
        },
    },
}


def choose_fighter(player_label: str) -> Fighter:
    print(f"\n{player_label}, აირჩიეთ მებრძოლი:")
    names = list(ROSTER.keys())

    for i, n in enumerate(names, 1):
        print(f"{i}. {n}")

    while True:
        choice = input("შენი არჩევანის ნომერი: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(names):
            name = names[int(choice) - 1]
            data = ROSTER[name]
            # ვაკეთებთ ახალ instance-ს, რომ ერთი და იგივე გმირის ორი ასლი დამოუკიდებლად მართავდეს თავის hp-ს
            return Fighter(name, data["hp"], data["power"], dict(data["skills"]))
        print("არასწორი არჩევანი, სცადე თავიდან.")


def choose_skill(fighter: Fighter) -> str:
    skills = list(fighter.skills.keys())
    print(f"\n{fighter.name}, აირჩიე skill:")

    for i, s in enumerate(skills, 1):
        print(f"{i}. {s}")

    while True:
        choice = input("skill-ის ნომერი: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(skills):
            return skills[int(choice) - 1]
        print("არასწორი არჩევანი, სცადე თავიდან.")


def play_game():
    player1 = choose_fighter("Player 1")
    player2 = choose_fighter("Player 2")

    print(f"\n=== ბრძოლა დაიწყო: {player1.name} VS {player2.name} ===")
    current, opponent = player1, player2  # player1 იწყებს

    while player1.is_alive() and player2.is_alive():
        skill = choose_skill(current)
        current.attack(opponent, skill)

        if not opponent.is_alive():
            print(f"\n{current.name} გაიმარჯვა!")
            break

        # rounds-ის შემოტრიალება
        current, opponent = opponent, current


if __name__ == "__main__":
    play_game()



# 3. შექმენით Earth კლასი, რომელიც იქნება მშობელი მინიმუმ 3 შვილის, თქვენი სურვილით უნდა დაწეროთ ისეთი ლოგიკა
# ამ კლასში რომ გამოყენებული გქონდეთ ობიექტზე ორიენტირებული პროგრამირების 4 პრინციპი, აბსტრაქცია, პოლიმორფიზმი,
# მრავალჯერადი მემკვიდრეობა & ენკაფსულაცია, შიდა ლოგიკა უნდა იყოს თანმიმდევრული, ანუ მაგალითად: class Animal-ში
# არ უნდა შეინახოთ შვილობილი class Engine. თავისუფალი ხართ შიგნით რას ჩაწერთ.

# იდეა:
# - Abstraction        -> LivingBeing არის აბსტრაქტული "ბაზა", რომელიც აღწერს
#                          რა ფუნქცია უნდა ჰქონდეს ყველა "ცოცხალ არსებას",
#                          კონკრეტული განხორციელების დაკონკრეტება შვილებზეა.
# - Encapsulation      -> Earth-ის შიდა state (__population, __resources)
#                          დაცულია "__" prefix-ით, გარედან პირდაპირ არ იცვლება.
# - Inheritance        -> Human, Animal, Plant ყველა შვილია LivingBeing-ის
#                          (Earth-ის "შინაარსი" თანმიმდევრულია: ყველა შვილი
#                          ცოცხალი არსებაა, არც ერთი არ არის Engine ან Rock).
# - Polymorphism       -> grow() მეთოდი თითო შვილში სხვადასხვანაირად მუშაობს.

class LivingBeing(ABC):
    """აბსტრაქტული ბაზა ყველა ცოცხალი არსებისთვის"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def grow(self) -> str:
        """ყველა ცოცხალი არსება იზრდება, თუმცა სხვადასხვანაირად (polymorphism)"""
        pass

    def describe(self) -> str:
        return f"{self.name} ({self.__class__.__name__})"


class Human(LivingBeing):
    def __init__(self, name: str, age: int = 0):
        super().__init__(name)
        self.age = age

    def grow(self) -> str:
        self.age += 1
        return f"{self.name} ერთი წლით გაიზარდა, ახლა {self.age} წლისაა."


class Animal(LivingBeing):
    def __init__(self, name: str, species: str):
        super().__init__(name)
        self.species = species

    def grow(self) -> str:
        return f"{self.name} ({self.species}) ხდება უფრო ძალიანი და სწრაფი."


class Plant(LivingBeing):
    def __init__(self, name: str, height_cm: float = 0):
        super().__init__(name)
        self.height_cm = height_cm

    def grow(self) -> str:
        self.height_cm += 2.5
        return f"{self.name} გაიზარდა {self.height_cm:.1f} სმ-მდე."


class Earth:
    """
        Earth — 'მშობელი' კლასი, რომელიც მართავს ცოცხალ არსებებს.
        დედამიწა არ არის ცოცხალი არსება, მაგრამ შეიცავს მათ.
    """

    def __init__(self):
        # Encapsulation: ეს ცვლადები დაცულია, გარედან პირდაპირი წვდომა არ აქვთ
        self.__inhabitants: list[LivingBeing] = []
        self.__resources: int = 1000  # თვითნებური "რესურსის" საზომი

    # public API, საშუალებას გვაძლევს კონტროლირებულად ვმართოთ private state
    def add_inhabitant(self, being: LivingBeing):
        self.__inhabitants.append(being)
        print(f"დედამიწაზე დაემატა: {being.describe()}")

    def get_population(self) -> int:
        return len(self.__inhabitants)

    def get_resources(self) -> int:
        return self.__resources

    def consume_resources(self, amount: int):
        if amount > self.__resources:
            print("საკმარისი რესურსი არ არის!")
            return
        self.__resources -= amount

    def simulate_year(self):
        print("\nერთი წელი გადის დედამიწაზე")

        for being in self.__inhabitants:
            print(being.grow())

        # ყოველ წელს მცირედით იხარჯება რესურსი
        self.consume_resources(10 * len(self.__inhabitants))
        print(f"დარჩენილი რესურსი: {self.__resources}")


if __name__ == "__main__":
    earth = Earth()

    earth.add_inhabitant(Human("გიორგი", age=25))
    earth.add_inhabitant(Animal("ლომი", species="Panthera leo"))
    earth.add_inhabitant(Plant("ვაშლის ხე", height_cm=120))

    print(f"\nმოსახლეობა: {earth.get_population()}")

    earth.simulate_year()
    earth.simulate_year()



# 4. ჯადოქარი
# მომხმარებელს აქვს 5 ინგრედიენტი: “ღამურა” , “ბუმბული”, “ვაშლი”, “ყვავილი”, “წყალი”. შეუძლია მხოლოდ
# 2-ის არჩევა და “მოხარშვა” ამ ორიდან უნდა გამოვიდეს რაღაც მაგალითად: “ვაშლი” + “წყალი” = “ვაშლის წვენი”
# და ასე შემდეგ. ყველა კომბინაცია უნდა იყოს განსხვავებული.

class Wizard:
    INGREDIENTS = ["ღამურა", "ბუმბული", "ვაშლი", "ყვავილი", "წყალი"]

    # ყველა შესაძლო წყვილის (5-დან 2-ის არჩევა = 10 კომბინაცია) რეცეპტი
    RECIPES = {
        frozenset(["ღამურა", "ბუმბული"]): "ღამის ფრთა (Night Wing potion)",
        frozenset(["ღამურა", "ვაშლი"]): "სიბნელის წვენი",
        frozenset(["ღამურა", "ყვავილი"]): "ბნელი ნექტარი",
        frozenset(["ღამურა", "წყალი"]): "ვამპირული ელექსირი",
        frozenset(["ბუმბული", "ვაშლი"]): "სიმსუბუქის ნაყენი",
        frozenset(["ბუმბული", "ყვავილი"]): "ფრენის ფხვნილი",
        frozenset(["ბუმბული", "წყალი"]): "ღრუბლის ცვარი",
        frozenset(["ვაშლი", "ყვავილი"]): "სამეფო ჯემი",
        frozenset(["ვაშლი", "წყალი"]): "ვაშლის წვენი",
        frozenset(["ყვავილი", "წყალი"]): "ყვავილოვანი ნახარში",
    }

    def __init__(self, name: str = "ჯადოქარი"):
        self.name = name

    def list_ingredients(self):
        print("შესაძლო ინგრედიენტები:")
        for i, ing in enumerate(self.INGREDIENTS, 1):
            print(f"{i}. {ing}")

    def brew(self, ingredient1: str, ingredient2: str) -> str:
        if ingredient1 == ingredient2:
            return "ერთი და იგივე ინგრედიენტის ორჯერ გამოყენება არ შეიძლება!"

        if ingredient1 not in self.INGREDIENTS or ingredient2 not in self.INGREDIENTS:
            return "უცნობი ინგრედიენტი!"

        key = frozenset([ingredient1, ingredient2])
        result = self.RECIPES.get(key, "უცნობი რეაქცია... ნაყენი ქრება კვამლად")
        return f"{ingredient1} + {ingredient2} = {result}"

    def choose_and_brew(self):
        self.list_ingredients()
        choices = []
        while len(choices) < 2:
            pick = input(f"აირჩიე ინგრედიენტი #{len(choices) + 1} (სახელით): ").strip()
            if pick in self.INGREDIENTS and pick not in choices:
                choices.append(pick)
            else:
                print("არასწორი ან გამეორებული არჩევანი, სცადე თავიდან.")

        print("\n" + self.brew(choices[0], choices[1]))


if __name__ == "__main__":
    wizard = Wizard()
    wizard.choose_and_brew()

    # სურვილისამებრ: ყველა შესაძლო კომბინაციის ნახვა ერთბაშად
    print("\nყველა შესაძლო კომბინაცია")
    for a, b in combinations(Wizard.INGREDIENTS, 2):
        print(wizard.brew(a, b))



# 5. ტრანსპორტირების სისტემა
# უნდა ავაწყოთ სისტემა, სადაც სხვადასხვა ტრანსპორტი (Car, Bus, Bike) იმართება ერთიანი კლასით Transport
# - ყველა ტრანსპორტს აქვს fuel, speed, capacity.
# - არის აბსტრაქტული მეთოდი move().
# - ყოველი transport სხვადასხვა წესით ხარჯავს საწვავს (პოლიმორფიზმი).
# - fuel ინახება private (ენკაფსულაცია).
# - ყველა transport იღებს ძირითად ფუნქციონალს Transport-იდან.(მემკვიდრეობა)

class Transport(ABC):
    def __init__(self, fuel: float, speed: int, capacity: int):
        self.__fuel = fuel  # encapsulation: name-mangled, არ ჩანს გარედან პირდაპირ
        self.speed = speed
        self.capacity = capacity

    # public "window" private fuel-ში წვდომისთვის
    def get_fuel(self) -> float:
        return self.__fuel

    def _consume_fuel(self, amount: float):
        """ protected helper — მხოლოდ subclass-ებს ჯერ კიდევ შეუძლიათ გამოყენება """
        self.__fuel = max(0.0, self.__fuel - amount)

    def refuel(self, amount: float):
        self.__fuel += amount
        print(f"{self.__class__.__name__}-ს ჩაესხა {amount}ლ საწვავი. ახლა აქვს {self.__fuel}ლ.")

    @abstractmethod
    def move(self, distance_km: float):
        """ ყველა transport-ი მოძრაობს, მაგრამ თითო თავისებურად ხარჯავს fuel-ს """
        pass

    def status(self):
        print(
            f"{self.__class__.__name__} | fuel: {self.__fuel:.1f}ლ | "
            f"speed: {self.speed}კმ/სთ | capacity: {self.capacity}"
        )


class Car(Transport):
    FUEL_PER_KM = 0.08  # ლ/კმ

    def __init__(self, fuel=40, speed=180, capacity=5):
        super().__init__(fuel, speed, capacity)

    def move(self, distance_km: float):
        needed = distance_km * self.FUEL_PER_KM
        if needed > self.get_fuel():
            print("Car-ს არ ჰყოფნის საწვავი ამ მანძილისთვის!")
            return
        self._consume_fuel(needed)
        print(f"Car გადაიარა {distance_km}კმ, დახარჯა {needed:.2f}ლ საწვავი.")


class Bus(Transport):
    FUEL_PER_KM = 0.25  # ავტობუსი მეტს ხარჯავს

    def __init__(self, fuel=120, speed=90, capacity=40):
        super().__init__(fuel, speed, capacity)

    def move(self, distance_km: float):
        needed = distance_km * self.FUEL_PER_KM
        if needed > self.get_fuel():
            print("Bus-ს არ ჰყოფნის საწვავი ამ მანძილისთვის!")
            return
        self._consume_fuel(needed)
        print(f"Bus გადაიარა {distance_km}კმ, დახარჯა {needed:.2f}ლ საწვავი.")


class Bike(Transport):
    # ველოსიპედს fuel არ ჭირდება ფიზიკურად, მაგრამ ვიდეო-თამაშისებურად
    # ვითვალისწინებთ "ენერგიას" საერთო ინტერფეისის შესანარჩუნებლად
    ENERGY_PER_KM = 0.02

    def __init__(self, fuel=10, speed=25, capacity=1):
        super().__init__(fuel, speed, capacity)

    def move(self, distance_km: float):
        needed = distance_km * self.ENERGY_PER_KM
        if needed > self.get_fuel():
            print("Bike-ს არ ჰყოფნის ენერგია ამ მანძილისთვის!")
            return
        self._consume_fuel(needed)
        print(f"Bike გადაიარა {distance_km}კმ, დახარჯა {needed:.2f} ერთეული ენერგია.")


if __name__ == "__main__":
    fleet = [Car(), Bus(), Bike()]

    for t in fleet:
        t.status()

    print()
    for t in fleet:
        t.move(50)

    print()
    for t in fleet:
        t.status()
