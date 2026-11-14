# CodeAlpha Python Task 2: Stock Portfolio Tracker

# Hardcoded stock prices (as allowed by the task)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130,
}


def get_portfolio():
    """Ask the user for stock names and quantities. Returns a dict."""
    portfolio = {}
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(STOCK_PRICES))
    print("Type 'done' when you have finished adding stocks.\n")

    while True:
        name = input("Enter stock name: ").strip().upper()

        if name == "DONE":
            break

        if name not in STOCK_PRICES:
            print("Stock not found. Choose from the available list.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity of {name}: "))
        except ValueError:
            print("Please enter a whole number.\n")
            continue

        if quantity <= 0:
            print("Quantity must be greater than 0.\n")
            continue

        # Adds up if the same stock is entered more than once
        portfolio[name] = portfolio.get(name, 0) + quantity

    return portfolio


def calculate_total(portfolio):
    """Return the total investment value."""
    return sum(STOCK_PRICES[s] * q for s, q in portfolio.items())


def build_summary(portfolio):
    """Build the summary text shown on screen and saved to file."""
    lines = ["--- Portfolio Summary ---"]
    for stock, qty in portfolio.items():
        value = STOCK_PRICES[stock] * qty
        lines.append(f"{stock}: {qty} shares x ${STOCK_PRICES[stock]} = ${value}")
    lines.append(f"\nTotal Investment Value: ${calculate_total(portfolio)}")
    return "\n".join(lines)


def save_summary(summary, filename="portfolio_summary.txt"):
    with open(filename, "w") as f:
        f.write(summary + "\n")
    print(f"\nSummary saved to {filename}")


def main():
    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered. Exiting.")
        return
    summary = build_summary(portfolio)
    print("\n" + summary)
    save_summary(summary)


if __name__ == "__main__":
    main()
