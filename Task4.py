#Task 4 Using map(): Apply GST toList of Prices
# 

prices = [100,250,400,1200,50]

prices_with_gst = list(map(lambda price: price + (price * 0.18), prices))
print("Prices before adding GST:", prices)
print("Prices after adding GST:", prices_with_gst)