import palindrome


def test_tacocat():
    assert palindrome.check_palindrome("tacocat") is True

def test_tacodog():
    assert palindrome.check_palindrome("tacodog") is False

def test_racecar():
    assert palindrome.check_palindrome("racecar") is True