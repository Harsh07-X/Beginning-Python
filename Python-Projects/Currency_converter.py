def currency_converter():
    
    rates = {
        "1": {"name": "EUR (Euro)", "rate": 0.0095},
        "2": {"name": "PR (Pakistan Rupee)", "rate":3.09 },
        "3": {"name": "GBP (British Pound)", "rate":0.0082},
        "4": {"name": "JPY (Japanese Yen)", "rate": 1.74},
        "5": {"name": "USD (US Dollar)", "rate": 0.011}
       
    }

    print("--- CURRENCY CONVERTER (Base: INR) ---")
    amount = float(input("Enter amount in INR: "))

    print("\nSelect the target currency:")
    for key, value in rates.items():
        print(f"{key}. {value['name']}")

   
    choice = input("\nEnter choice (1-5): ")

   
    if choice in rates:
        selected_currency = rates[choice]["name"]
        exchange_rate = rates[choice]["rate"]
        result = amount * exchange_rate
        
        print("-" * 30)
        print(f"Result: {amount} INR = {result:.2f} {selected_currency}")
        print("-" * 30)
    else:
        print("Invalid selection!")

if __name__ == "__main__":
    currency_converter()