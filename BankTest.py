from bank import Account
import pytest

def test_deposit():
    acc = Account("Ana", 100)
    assert acc.deposit(50) == 150

def test_withdraw():
    acc = Account("Ana", 100)
    assert acc.withdraw(40) == 60

def test_withdraw_insufficient_balance():
    acc = Account("Ana", 100)
    with pytest.raises(ValueError):
        acc.withdraw(200)