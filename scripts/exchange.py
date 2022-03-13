def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money to exchange
    :param exchange_value: float - amount of domestic 
    currency equal to one unit of foreign currency
    :return: float - the budget's value in the foreign currency
    """
    return budget / exchange_rate


def get_change(budget, exchange_value):
    """
    :param budget: float - amount of money before exhange
    :param exchanging_value: float - the amount tha tis taken from the budget
    to be exhcanged
    :return: float - the amount of money that is left from the bodget
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
