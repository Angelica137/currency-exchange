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
