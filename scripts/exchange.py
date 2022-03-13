def exchange_money(budget: float, exchange_rate: float) -> float:
    """
    :param budget: float - amount of money to exchange
    :param exchange_value: float - amount of domestic 
    currency equal to one unit of foreign currency
    :return: float - the budget's value in the foreign currency
    """
    return budget / exchange_rate
