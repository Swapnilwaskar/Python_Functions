#Task 6 Combined utility function
# Write a function process_prices

def process_prices(prices):
    discounted_prices = list(map(lambda price: price - (price * 0.10), prices))
    filtered_prices = list(filter(lambda price: price > 300, discounted_prices))
    
    #return both discounted and filtered prices
    return discounted_prices, filtered_prices

print(process_prices([100, 250, 400, 1200, 50, 2000, 850]))
    
