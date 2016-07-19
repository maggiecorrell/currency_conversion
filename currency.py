class Currency:

    def __init__(self, amount, currency_code = 'USD'):
        currency_code_dict = {'$': 'USD', '€': 'EUR', '¥': 'JPY'}
        print(type(amount))
        if type(amount) == str:
            sign = amount[0]
            currency_code = currency_code_dict[sign]
            amount = int(amount[1:])
            print(sign)
        self.amount = amount
        self.currency_code = currency_code


    def __eq__(self, other):
        return self.amount == other.amount and \
                self.currency_code == other.currency_code

    def __add__(self, other):
        if self.currency_code != other.currency_code:
            raise DifferentCurrencyCodeError
        return (self.amount + other.amount, self.currency_code)

    def __sub__(self, other):
        if self.currency_code != other.currency_code:
            raise DifferentCurrencyCodeError
        return (self.amount - other.amount, self.currency_code)

    def __mul__(self, enter_num):
        return (self.amount * float(enter_num), self.currency_code)



class DifferentCurrencyCodeError(Exception):
    pass
