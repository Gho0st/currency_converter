# currency_converter.py
# Program to convert COP, PEN, BRL to USD

# Current exchange rate in USD
rate_cop = 0.0002576   # Colombian Peso
rate_pen = 0.2876      # Peruvian Sol
rate_brl = 0.1876      # Brazilian Real

# Ask user for amounts
cop = float(input("Enter amount in COP(Colombian pesos): "))
pen = float(input("Enter amount in PEN(Peruvian soles): "))
brl = float(input("Enter amount in BRL(Brazilian reais): "))

# Converts to USD
usd_from_cop = cop * rate_cop
usd_from_pen = pen * rate_pen
usd_from_brl = brl * rate_brl

# Display results
print(f"{cop} COP = ${usd_from_cop:.2f} USD")
print(f"{pen} PEN = ${usd_from_pen:.2f} USD")
print(f"{brl} BRL = ${usd_from_brl:.2f} USD")