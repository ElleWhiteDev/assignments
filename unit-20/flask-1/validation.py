from forex_python.converter import CurrencyCodes


def validate_currency_code(code):
    currency = CurrencyCodes().get_currency_name(code)

    if currency is None:
        raise ValueError("Invalid currency code")
    return currency


def is_valid_amount(amount):
    amount = float(amount)
    if amount >= 0:
        return True
    else:
        return False
