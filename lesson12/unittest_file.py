# === imports ===
import unittest as utest


# 1. unittest1
# შექმენით Calculator კლასი add, subtract, multiply, divide მეთოდებით. დაწერეთ unittest რომელიც ამოწმებს
# ყველა მეთოდს. გაითვალისწინეთ 0-ზე გაყოფაც. გამოიყენეთ unittest მოდული გამოიყენეთ setup მეთოდი.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("0-ზე გაყოფა დაუშვებელია")
        return a / b


class TestCalculator(utest.TestCase):
    def setUp(self):
        # ეს მეთოდი გაეშვება ყოველი ტესტის წინ
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)



# 2. unittest2
# შექმენით BankAccount კლასი deposit და withdraw მეთოდებით. დაწერეთ unittest რომელიც ამოწმებს:
# - სწორი ბალანსი; - უარყოფითი თანხის შეტანისას შეცდომა; - თანხის გამოტანა ბალანსზე მეტისას შეცდომა

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("თანხა არ შეიძლება იყოს უარყოფითი")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("არასაკმარისი ბალანსი")
        self.balance -= amount
        return self.balance


class TestBankAccount(utest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)

    def test_deposit_correct_balance(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_negative_raises_error(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-20)

    def test_withdraw_correct_balance(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_withdraw_more_than_balance_raises_error(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1000)



# 3. unittest3
# შექმენით ფუნქცია რომელიც იღებს JSON (dict) response-ს და აბრუნებს "status"-ის მნიშვნელობას.
# თუ status არ არსებობს → შეცდომა. დაწერეთ ტესტები

def get_status(response: dict):
    if "status" not in response:
        raise KeyError("'status' არ მოიძებნა response-ში")
    return response["status"]


class TestGetStatus(utest.TestCase):
    def test_status_exists(self):
        response = {"status": "ok", "code": 200}
        self.assertEqual(get_status(response), "ok")

    def test_status_missing_raises_error(self):
        response = {"code": 404}
        with self.assertRaises(KeyError):
            get_status(response)

    def test_status_empty_dict_raises_error(self):
        with self.assertRaises(KeyError):
            get_status({})

if __name__ == "__main__":
    test.main()
