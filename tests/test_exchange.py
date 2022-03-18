from scripts.exchange import *


def test_exchange_money():
    assert exchange_money(127.5, 1.2) == 106.25


def test_get_change():
    assert get_change(127.5, 120) == 7.5


def test_get_change_458000():
    assert get_change(463000, 5000) == 458000


def test_get_value_of_bills():
    assert get_value_of_bills(5, 128) == 640


def test_get_number_of_bills():
    assert get_number_of_bills(127.5, 5) == 25


def test_exchangeable_value_returns_80():
    assert exchangeable_value(127.25, 1.20, 10, 20) == 80


def test_exchange_value_returns_95():
    assert exchangeable_value(127.25, 1.20, 10, 5) == 95


def test_exchangeable_value_8568():
    assert exchangeable_value(100000, 10.61, 10, 1) == 8568


def test_exchangeable_value_1400():
    assert exchangeable_value(1500, 0.84, 25, 40) == 1400


def test_non_exchangeable_value_16():
    assert non_exchangeable_value(127.25, 1.20, 10, 20) == 16


def test_non_exchangeable_value_1():
    assert non_exchangeable_value(127.25, 1.20, 10, 5) == 1
