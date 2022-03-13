from scripts.exchange import *


def test_exchange_money():
    assert exchange_money(127.5, 1.2) == 106.25


def test_get_change():
    assert get_change(127.5, 120) == 7.5


def test_get_value_of_bills():
    assert get_value_of_bills(5, 128) == 640
