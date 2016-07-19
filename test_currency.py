from currency import Currency
from currency import DifferentCurrencyCodeError
from nose.tools import assert_raises

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

def test_raise_a_different_currency_code_error_when_adding():
    curr1 = Currency(50, 'USD')
    curr2 = Currency(50, 'EUR')

    assert_raises(DifferentCurrencyCodeError, Currency.__add__, curr1, curr2 )

def test_raise_a_different_currency_code_error_when_subtracting():
    curr1 = Currency(100, 'USD')
    curr2 = Currency(50, 'EUR')

    assert_raises(DifferentCurrencyCodeError, Currency.__sub__, curr1, curr2 )

def test_multiply_by_int():
    curr1 = Currency(100, 'USD')
    enter_number = 9

    assert  curr1 * enter_number == (900, 'USD')

def test_multiply_by_float():
    curr1 = Currency(100, 'USD')
    enter_number = 1.97

    assert  curr1 * enter_number == (197, 'USD')

def test_currency_symbol():
    curr1 = Currency('€5')
    curr2 = Currency(5, 'EUR')

    assert curr1 == curr2
