# Simple Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 120
}

portfolio = {}

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' when you are finished.\n")

while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid symbol. Try again.")
        continue

    try:
        qty = int(input(f"Enter quantity for {stock}: "))
    except:
        print("Please enter a number.")
        continue

    if qty <= 0:
        print("Quantity must be more than zero.")
        continue

    if stock in portfolio:
        portfolio[stock] += qty
    else:
        portfolio[stock] = qty

if not portfolio:
    print("\nNo stocks entered.")
else:
    total = 0
    print("\nYour Portfolio Summary:")
    print("-" * 30)
    for s, q in portfolio.items():
        price = stock_prices[s]
        value = price * q
        total += value
        print(f"{s} - Qty: {q}, Price: ${price}, Total: ${value}")
    print("-" * 30)
    print("Total Investment: $", total)

    save = input("\nDo you want to save this summary to a file? (y/n): ").lower()
    if save == "y":
        with open("portfolio_summary.txt", "w") as f:
            f.write("Portfolio Summary\n")
            f.write("-" * 30 + "\n")
            for s, q in portfolio.items():
                price = stock_prices[s]
                value = price * q
                f.write(f"{s} - Qty: {q}, Price: ${price}, Total: ${value}\n")
            f.write("-" * 30 + "\n")
            f.write(f"Total Investment: ${total}\n")
        print("Saved to portfolio_summary.txt")
