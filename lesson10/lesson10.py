import random

# 1. შექმენი თამაში
# შექმენით Character კლასი (სახელი, სიცოცხლე, ძალა) გააკეთეთ მემკვიდრეები: Warrior, Mage, Archer გამოიყენეთ
# super() რომ მშობლის კონსტრუქტორი გამოიძახოთ თამაში: ორი გმირი ებრძვის ერთმანეთს (attack() მეთოდი). Warrior
# სჯობს Mage-ს, Mage სჯობს Archer-ს, Archer სჯობს Warrior-ს ტესტირების დროს სცადე სამივე ვარიანტი, ანუ როცა
# ერთმანეთზე გააკეთებინებ შეტევას 1 უნდა დამარცხდეს და 1მა გაიმარჯვოს, ეს უნდა გამოიტანო ტერმინალში. ზედმეტი
# ვალიდაციები და პირობის შეცვლა არაა საჭირო. რაც პირობაში წერია ამ მონახაზით გააკეთეთ თავისუფლად.

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    # შეტევის მეთოდი
    def attack(self, enemy):
        damage = self.power

        # Warrior სჯობს Mage-ს
        if isinstance(self, Warrior) and isinstance(enemy, Mage):
            damage *= 2

        # Mage სჯობს Archer-ს
        elif isinstance(self, Mage) and isinstance(enemy, Archer):
            damage *= 2

        # Archer სჯობს Warrior-ს
        elif isinstance(self, Archer) and isinstance(enemy, Warrior):
            damage *= 2

        enemy.health -= damage

        print(f"{self.name} attacked {enemy.name} and dealt {damage} damage.")
        print(f"{enemy.name}'s health: {enemy.health}")

        if enemy.health <= 0:
            print(f"{enemy.name} was defeated!")
            print(f"{self.name} is the winner!\n")


# Warrior კლასი
class Warrior(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)


# Mage კლასი
class Mage(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)


# Archer კლასი
class Archer(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)


# ------------------------- Warrior vs Mage -------------------------
print("=== Warrior vs Mage ===")

warrior = Warrior("Thor", 100, 60)
mage = Mage("Merlin", 100, 30)

warrior.attack(mage)


# ------------------------- Mage vs Archer -------------------------
print("=== Mage vs Archer ===")

mage = Mage("Gandalf", 100, 60)
archer = Archer("Legolas", 100, 30)

mage.attack(archer)


# ------------------------- Archer vs Warrior -------------------------
print("=== Archer vs Warrior ===")

archer = Archer("Robin", 100, 60)
warrior = Warrior("Conan", 100, 30)

archer.attack(warrior)



# 2. პატარა პროგრამა მონსტრებზე
# თქვენი ვალია შექმნათ მონსტრების ქარხანა სადაც: შექმენით Monster კლასი. დაამატეთ classmethod create_from_level(level),
# რომელიც ქმნის მონსტრს სიძლიერის მიხედვით. სხვადასხვა level -> სხვადასხვა ტიპის მონსტრი. შექმენი მინიმუმ 10 მონსტრი
# რომლებსაც ექნებათ სახელები, სახელები არ უნდა იყოს ბოროტული :) (ეს მონსტრები ეხმარებიან ადამიანებს) “აქაც იგივე”
# არაასაჭირო ზედმეტი ვალიდაციები და პირობის ცვლილება. ამ მონახაზში იმუშავეთ თავისუფლად.

class Monster:
    def __init__(self, name, level, strength):
        self.name = name
        self.level = level
        self.strength = strength

    @classmethod
    def create_from_level(cls, name, level):
        # მონსტრის სიძლიერე level-ის მიხედვით
        if level <= 3:
            strength = 20
        elif level <= 6:
            strength = 50
        else:
            strength = 100

        return cls(name, level, strength)

    def show_info(self):
        print(
            f"Name: {self.name}, "
            f"Level: {self.level}, "
            f"Strength: {self.strength}"
        )


# 10 მეგობრული მონსტრი
monster1 = Monster.create_from_level("Sunny", 1)
monster2 = Monster.create_from_level("Cloudy", 2)
monster3 = Monster.create_from_level("Buddy", 3)
monster4 = Monster.create_from_level("Spark", 4)
monster5 = Monster.create_from_level("Happy", 5)
monster6 = Monster.create_from_level("Lucky", 6)
monster7 = Monster.create_from_level("Rainbow", 7)
monster8 = Monster.create_from_level("Star", 8)
monster9 = Monster.create_from_level("Angel", 9)
monster10 = Monster.create_from_level("Smile", 10)

# სია
monsters = [
    monster1,
    monster2,
    monster3,
    monster4,
    monster5,
    monster6,
    monster7,
    monster8,
    monster9,
    monster10
]

# ინფორმაციის გამოტანა
for monster in monsters:
    monster.show_info()



# 3. მარტივი კაზინო თამაში
# შექმენით SlotMachine კლასი. გამოიყენეთ staticmethod შემთხვევითი სიმბოლოების დასაგენერირებლად. გამოიყენეთ
# classmethod from_difficulty(level) -> უფრო რთული დონის სლოტები მოთამაშე მოიგებს თუ სამივე სიმბოლო დაემთხვევა.
# აუცილებლად გატესტეთ, სცადეთ რამოდენიმე ვარიანტის გაშვება.

class SlotMachine:
    def __init__(self, symbols):
        self.symbols = symbols

    @staticmethod
    def generate_symbol(symbols):
        return random.choice(symbols)

    @classmethod
    def from_difficulty(cls, level):
        # რაც უფრო მაღალია დონე, მით მეტი სიმბოლოა და მოგებაც რთულდება

        if level == "easy":
            symbols = ["🍎", "🍌", "🍇"]

        elif level == "medium":
            symbols = ["🍎", "🍌", "🍇", "🍒", "🍉"]

        else:  # hard
            symbols = ["🍎", "🍌", "🍇", "🍒", "🍉", "⭐", "💎"]

        return cls(symbols)

    def play(self):
        result = [
            self.generate_symbol(self.symbols),
            self.generate_symbol(self.symbols),
            self.generate_symbol(self.symbols)
        ]

        print(" | ".join(result))

        if result[0] == result[1] == result[2]:
            print("You Win!\n")
        else:
            print("You Lose!\n")


# ------------------- Easy -------------------
print("=== EASY SLOT ===")
easy_slot = SlotMachine.from_difficulty("easy")

for _ in range(3):
    easy_slot.play()


# ------------------- Medium -------------------
print("=== MEDIUM SLOT ===")
medium_slot = SlotMachine.from_difficulty("medium")

for _ in range(3):
    medium_slot.play()


# ------------------- Hard -------------------
print("=== HARD SLOT ===")
hard_slot = SlotMachine.from_difficulty("hard")

for _ in range(3):
    hard_slot.play()



# 4. გმირის ქულების სისტემა
# შექმენით Hero კლასი. private health, private score. staticmethod random_event() -> შემთხვევითი მოვლენა
# (ქულა ემატება ან ჯანმრთელობა აკლდება). classmethod from_name(cls, name) -> ქმნის გმირს სახელით. მემკვიდრე
# SuperHero -> დამატებითი ძალა. super() გამოიძახეთ მშობლის კონსტრუქტორისთვის. თამაში გრძელდება სანამ გმირის health > 0.

class Hero:
    def __init__(self, name):
        self.name = name
        self.__health = 100
        self.__score = 0

    @staticmethod
    def random_event():
        return random.choice(["score", "health"])

    @classmethod
    def from_name(cls, name):
        return cls(name)

    def play(self):
        event = self.random_event()

        if event == "score":
            self.__score += 10
            print(f"{self.name} მიიღო +10 ქულა.")
        else:
            self.__health -= 20
            print(f"{self.name}-ს დააკლდა 20 ჯანმრთელობა.")

        print(f"Health: {self.__health}")
        print(f"Score: {self.__score}")
        print("-" * 30)

    def is_alive(self):
        return self.__health > 0


class SuperHero(Hero):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power


# classmethod-ის გამოყენებით გმირის შექმნა
hero = SuperHero("Batman", "Super Strength")

print(f"Hero: {hero.name}")
print(f"Power: {hero.power}")
print("-" * 30)

# თამაში გრძელდება სანამ health > 0
while hero.is_alive():
    hero.play()

print(f"{hero.name} დამარცხდა!")



# 5. პროგრამა კარტზე
# Card კლასი (rank, suit). Deck კლასი -> private cards list. classmethod create_standard_deck()
# აბრუნებს სტანდარტულ 52 კარტიან დასტას. staticmethod shuffle(cards) აურევს კარტებს. მოთამაშე იღებს 5 კარტს
# და ამოწმებს, აქვს თუ არა “მარტივი კომბინაცია” (მაგ: ორი ერთნაირი) აუცილებლად გატესტეთ კოდი, შეასრულეთ
# მხოლოდ პირობაში მოცემული ვარიანტი, არაა საჭირო დამატება.

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self, cards):
        self.__cards = cards

    @classmethod
    def create_standard_deck(cls):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        cards = [Card(rank, suit) for suit in suits for rank in ranks]
        return cls(cards)

    @staticmethod
    def shuffle(cards):
        random.shuffle(cards)
        return cards

    def draw(self, n=5):
        drawn = self.__cards[:n]
        self.__cards = self.__cards[n:]
        return drawn


# ----------------------- თამაში -----------------------
deck = Deck.create_standard_deck()

# shuffle
deck._Deck__cards = Deck.shuffle(deck._Deck__cards)

# 5 კარტის აღება
hand = deck.draw(5)

print("Player hand:")
for card in hand:
    print(card)

# მარტივი კომბინაცია: ორი ერთნაირი rank
ranks = [card.rank for card in hand]

if len(ranks) != len(set(ranks)):
    print("\nYou have a simple combination (pair found)!")
else:
    print("\nNo combination found.")
