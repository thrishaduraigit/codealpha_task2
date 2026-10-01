# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

total_investment = 0

print("----- Stock Portfolio Tracker -----")

while True:

    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:

        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock]

        investment = price * quantity

        total_investment = total_investment + investment

        print("Stock Price:", price)
        print("Investment Value:", investment)

    else:
        print("Stock not found in the list.")

print("\n----- Portfolio Summary -----")
print("Total Investment:", total_investment)

# Save the result in a text file
file = open("portfolio.txt", "w")

file.write("Stock Portfolio Summary\n")
file.write("-----------------------\n")
file.write("Total Investment: " + str(total_investment))

file.close()

print("Portfolio saved successfully in portfolio.txt")
