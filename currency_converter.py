# Currency Converter

rates = {
    "GBP": 1,
    "USD": 1.27,
    "EUR": 1.16,
    "JPY": 188.50
}

print("Available currencies:")
for currency in rates:
    print(currency)

from_currency = input("Convert from: ").upper()
to_currency = input("Convert to: ").upper()

amount = float(input("Amount: "))

if from_currency in rates and to_currency in rates:
    
    gbp_amount = amount / rates[from_currency]
    
    converted = gbp_amount * rates[to_currency]

    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")

else:
    print("Invalid currency code.")
