from currency_converter import CurrencyConverter, UnknownCurrencyCodeError
from currency import Currency
from nose.tools import assert_raises

conversion_rates = {'USD': 1.0 , 'EUR': 0.9, 'JPY': 106}

def test_create_currency_with_code_and_rates():
    converter = CurrencyConverter(conversion_rates)

    assert converter.rates == conversion_rates

def test_currency_code_that_is_equal_to_passed_in():
    converter = CurrencyConverter(conversion_rates)
    currency = Currency(1, 'USD')
    convert_to_code = 'USD'
    result = converter.convert(currency, convert_to_code)

    assert result == Currency(1, 'USD')

def test_diff_currency_code_that_passed_in():
    converter = CurrencyConverter(conversion_rates)
    currency = Currency(1, 'USD')
    convert_to_code = 'JPY'
    result = converter.convert(currency, convert_to_code)

    assert result == Currency(106, 'JPY')

def test_raise_error_unknown():
    converter = CurrencyConverter(conversion_rates)
    currency = Currency(1, 'USD')
    convert_to_code = "GBP"

    with assert_raises(UnknownCurrencyCodeError):
         converter.convert(currency, convert_to_code)
