# Task 7 Mini Problem: Menu Using Functions
#create the functions add_price(prices_list, price),
#get_average_price(prices_list), get_max_price(prices_list), get_min_price(prices_list)
prices_list = []
def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    if prices_list:
        return sum(prices_list) / len(prices_list)
    else:
        return 0

def get_max_price(prices_list):
    if prices_list:
        return max(prices_list)
    else:
        return 0

def get_min_price(prices_list):
    if prices_list:
        return min(prices_list)
    else:
        return 0
    
while True:
    print("\nMenu:")
    print("1. Add Price")
    print("2. Get Average Price")
    print("3. Get Maximum Price")
    print("4. Get Minimum Price")
    print("q. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        price = float(input("Enter the price to add: "))
        add_price(prices_list, price)
        print(f"Price {price} added.")
        print("Current Prices List:", prices_list)

    elif choice == '2':
        if prices_list:
            average_price = get_average_price(prices_list)
            print(f"Average Price: {average_price}")
        else:
            print("No prices available to calculate average.")

    elif choice == '3':
        if prices_list:
            max_price = get_max_price(prices_list)
            print(f"Maximum Price: {max_price}")
        else:
            print("No prices available to find maximum.")

    elif choice == '4':
        get_min_price = get_min_price(prices_list)
        print(f"Minimum Price: {get_min_price}")

    elif choice == 'q':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")

