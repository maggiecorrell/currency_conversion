from currency_converter import CurrencyConverter

def test_request_currency_code_that_is_equal_to_passed_in():
    assert currency_converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD')
