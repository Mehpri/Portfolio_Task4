def currency_converter(amount,from_currency,to_currency):
    conversion_rate = {
'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
}
    rate = (conversion_rate[from_currency][to_currency])
    converted = round((amount * rate),2)
    print(converted)

amount = int(input("Enter in the numerical amount you want converting:"))
from_currency, to_currency = input("Enter the currency code for the currency you're converting from and what you want to convert to:").split()

currency_converter(amount,from_currency,to_currency)
    