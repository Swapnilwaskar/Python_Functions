#Lambda Function: GST Calculator
# Create a lambda function gst that returns price after adding 18% GST.
gst = lambda price: price + (price * 0.18)
print("Price after adding (18%) GST on 1000:", gst(1000))

gst_with_discount = lambda price, discount_percent=5: price - (price * discount_percent / 100) + (price - (price * discount_percent / 100)) * 0.18
print("Price after (10%) discount and adding (18%) GST on 1000:", gst_with_discount(1000, 10))