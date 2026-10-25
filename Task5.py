#Task 5 Using filter(): Filter Expensive Products

prices = [100, 250, 400, 1200, 50, 2000, 850]

prices_above_500 = list(filter(lambda price: price > 500, prices))
print("Prices above 500:", prices_above_500)

prices_below_500 = list(filter(lambda price: price < 500, prices))
print("Prices below 500:", prices_below_500)