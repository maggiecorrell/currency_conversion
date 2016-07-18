from currency import Currency

def test_create_currency_with_amount_and_code():
    one_dollar = Currency(1, 'USD')

    assert one_dollar.amount == 1
    assert one_dollar.currency_code == 'USD'

def test_currencys_can_be_equal():
    curr1 = Currency(99, 'USD')
    curr2 = Currency(99, 'USD')

    assert curr1 == curr2

def test_currencys_with_different_amounts_are_not_equal():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(99, 'USD')

    assert curr1 != curr2

def test_currencys_with_different_currency_codes_are_not_equal():
    curr1 = Currency(1, 'USD')
    curr2 = Currency(1, 'EUR')

    assert curr1 != curr2

def test_add_currency_with_same_currency_code():
    curr1 = Currency(56, 'USD')
    curr2 = Currency(44, 'USD')

    assert curr1 + curr2 == (100, 'USD')

def test_subtract_currency_with_same_currency_code():
    curr1 = Currency(136, 'USD')
    curr2 = Currency(44, 'USD')

    assert curr1 - curr2 == (92, 'USD')
