def discount_table():
    for price in (4.95, 9.95, 14.95, 19.95, 24.95):
        print(f"Original price: {price:.2f}")
        print(f"Discount amount: {price * 0.6:.2f}")
        print(f"New price: {price * 0.4:.2f}")
        print()
