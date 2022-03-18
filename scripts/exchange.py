def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money to exchange
    :param exchange_rate: float - amount of domestic currency
    equal to one unit of foreign currency
    :return: float - the budget's value in the foreign currency
    """
    return budget / exchange_rate


def get_change(budget, exchange_value):
    """
    :param budget: float - amount of money before exhange
    :param exchange_value: float - the amount that is taken
    from the budget to be exhcanged
    :return: float - the amount of money that is left from the budget
    """
    return budget - exchange_value


def get_value_of_bills(denomination, number_of_bills) -> int:
    """
    :param denomination: int - the value of a single bill
    :param number_of_bills: int - Numbner of bills received
    :return: int - Amount of money returned
    """
    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """
    :param budget: float - amount of money to be exchanged
    :param denomination: int - the value of a single bill
    :return: the number of new currency bills that are received
    """
    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - amount of money to be exchanged
    :param exchange_rate: float - amount of domestic currency
    equal to one unit of foreign currency
    :param spread: int - the percentage taken as an exchange fee
    expressed as an integer
    :param denomination: int - the value of a single bill
    :return: the maximum value of the new currency in bills only
    => removes the petty change
    """
    true_rate = exchange_rate + exchange_rate * (spread / 100)
    exchange_value = exchange_money(budget, true_rate)
    number_of_bills = get_number_of_bills(exchange_value, denomination)
    return get_value_of_bills(denomination, number_of_bills)


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    This exchange booth keps the change in addition to chargin the commision
    :return: int - the value that is not exchangeable
    """
    true_rate = exchange_rate + exchange_rate * (spread / 100)
    exchange_value = exchange_money(budget, true_rate)
    amount_returned = exchangeable_value(
        budget, exchange_rate, spread, denomination)
    return int(exchange_value - amount_returned)
