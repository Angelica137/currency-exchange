from scripts.exchange import *


def test_exchange_money():
    assert exchange_money(127.5, 1.2) == 106.25
