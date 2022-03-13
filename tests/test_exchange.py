from scripts.exchange import *


def test_exchange_money():
    assert exchange_money(127.5, 1.2) == 106.25


def test_get_change():
    assert get_change(127.5, 120) == 7.5


def test_get_value_of_bills():
    assert get_value_of_bills(5, 128) == 640


def test_get_number_of_bills():
    assert get_number_of_bills(127.5, 5) == 25


def test_exchange_value_returns_80():
    assert exchange_value(127.25, 1.20, 10, 20) == 80


def test_exchange_value_returns_95():
    assert exchange_value(127.25, 1.20, 10, 5) == 95
