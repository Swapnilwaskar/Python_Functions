# Task 1 Basic Function: Price After Discount

# write the function apply_discount(price,discount_percent)

def apply_discount(price,discount_percent=5):
    if(discount_percent <=60):
        discount_price = price * (discount_percent/100)
        return price - discount_price
    else:
        return price
print("Price after (10%) discount on 1000:", apply_discount(1000, 10))
print("Price using default discount (5%) on 500:", apply_discount(500))
print("Price after (70%) discount on 1000:", apply_discount(1000, 70))
print("Price using default discount (5%) on 1000:", apply_discount(1000))