import pytest
from bank_account import BankAccount


def test_deposit():
    account = BankAccount(100)

    assert account.deposit(50) == 150


def test_withdraw():
    account = BankAccount(100)

    assert account.withdraw(30) == 70


def test_get_balance():
    account = BankAccount(200)

    assert account.get_balance() == 200


def test_transfer():
    account1 = BankAccount(200)
    account2 = BankAccount(100)

    account1.transfer(account2, 50)

    assert account1.get_balance() == 150
    assert account2.get_balance() == 150


def test_negative_deposit():
    account = BankAccount(100)

    with pytest.raises(ValueError):
        account.deposit(-50)


def test_insufficient_balance():
    account = BankAccount(100)

    with pytest.raises(ValueError):
        account.withdraw(200)
