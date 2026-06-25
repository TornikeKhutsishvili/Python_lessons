# === imports ===
import pytest as ptest


# 4. pytest1
# შექმენით ფუნქცია Celsius → Fahrenheit. დაწერეთ pytest ტესტები approx-ის გამოყენებით. ნიმუში: assert pytest.approx

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def test_zero_celsius():
    assert celsius_to_fahrenheit(0) == ptest.approx(32)

def test_boiling_point():
    assert celsius_to_fahrenheit(100) == ptest.approx(212)

def test_negative_celsius():
    assert celsius_to_fahrenheit(-40) == ptest.approx(-40)

def test_decimal_celsius():
    # approx გამოგვადგება float-ის მცირე ცდომილებებისთვის
    assert celsius_to_fahrenheit(37.5) == ptest.approx(99.5, rel=1e-3)



# 5. pytest2
# შექმენით ფუნქცია რომელიც ამოწმებს მომხმარებლის ლოგინს და პაროლს dictionary-დან pytest-ში გამოიყენეთ raises შეცდომის
# დასატესტად. ნიმუში: raise ValueError

users_db = {
    "tornike": "tornike123",
    "ana": "Anaana",
    "levan": "levanlevan",
    "mariami": "mariam1234"
}

def check_login(username, password):
    if username not in users_db:
        raise ValueError("მომხმარებელი არ მოიძებნა")
    if users_db[username] != password:
        raise ValueError("პაროლი არასწორია")
    return True

def test_correct_login():
    assert check_login("tornike", "tornike123") is True

def test_wrong_password_raises_error():
    with ptest.raises(ValueError, match="პაროლი არასწორია"):
        check_login("tornike", "wrongpass")

def test_nonexistent_user_raises_error():
    with ptest.raises(ValueError, match="მომხმარებელი არ მოიძებნა"):
        check_login("giorgi", "1234")



# 6. pytest3
# დაწერეთ ფუნქცია, რომელიც ამოწმებს არის თუ არა სტრიქონი სწორი email (ანუ შეიცავს @ და . სიმბოლოებს)
# pytest-ით გააკეთეთ ტესტები parametrization-ის გამოყენებით. ნიმუში: @pytest.mark.parametrize

def is_valid_email(email):
    return "@" in email and "." in email

@ptest.mark.parametrize("email, expected", [
    ("test@gmail.com", True),
    ("user.name@domain.co", True),
    ("invalid-email.com", False),     # არ აქვს @
    ("invalid@domain", False),        # არ აქვს .
    ("", False),                      # ცარიელი სტრიქონი
    ("a@b.c", True),
    ("plainaddress", False),
])

def test_is_valid_email(email, expected):
    assert is_valid_email(email) == expected
