"""Input-safe helpers for coffee-shop menu codes and order modifiers."""

MENU_PRICES = {"LAT": 4.50, "CAP": 4.00, "ESP": 3.00, "AME": 3.50, "MOC": 5.00}


def lookup_drink_code(code_string):
    """Return a drink price for a three-letter code; reject unknown input."""
    if not isinstance(code_string, str):
        raise ValueError("Drink code must be text")
    code_prefix = code_string.strip().upper()[:3]
    if code_prefix not in MENU_PRICES:
        raise ValueError(f"Unknown drink code: {code_prefix!r}")
    return MENU_PRICES[code_prefix]


def calculate_average_shot_cost(pricing_csv):
    """Return the arithmetic mean of comma-separated non-negative prices."""
    if not isinstance(pricing_csv, str) or not pricing_csv.strip():
        raise ValueError("Pricing data must be a non-empty CSV string")
    try:
        prices = [float(part.strip()) for part in pricing_csv.split(",")]
    except (TypeError, ValueError) as exc:
        raise ValueError("Every shot price must be numeric") from exc
    if not prices or any(price < 0 or price != price or price in (float("inf"), float("-inf")) for price in prices):
        raise ValueError("Shot prices must be finite and non-negative")
    return sum(prices) / len(prices)


def parse_order_modifiers(order_spec):
    """Parse semicolon-separated key:value pairs with strict validation."""
    if not isinstance(order_spec, str) or not order_spec.strip():
        raise ValueError("Order modifiers must be a non-empty string")
    modifier_dict = {}
    for item in order_spec.split(";"):
        if not item.strip() or ":" not in item:
            raise ValueError("Each modifier must contain a key and value separated by ':'")
        key, value = item.split(":", 1)
        key, value = key.strip(), value.strip()
        if not key or not value:
            raise ValueError("Modifier keys and values cannot be empty")
        if key in modifier_dict:
            raise ValueError(f"Duplicate modifier: {key}")
        modifier_dict[key] = value
    return modifier_dict


def main():
    print("==== Running lookup_drink_code ====")
    try:
        print("Base Price: $", lookup_drink_code(input("Enter drink code prefix: ")))
        print("Average Shot Price: $", calculate_average_shot_cost(input("Enter CSV of shot prices: ")))
        print("Parsed Modifiers:", parse_order_modifiers(input("Enter modifiers: ")))
    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
