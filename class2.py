class Zomato:

    # Class variables
    discount = 10
    coupon = "ZOMATO50"
    restaurant_names = set()
    restaurant_number = 0

    def __init__(self, restaurant_name, items):

        # Instance variables
        self.restaurant_name = restaurant_name
        self.items = items

        # Generate restaurant ID
        Zomato.restaurant_number += 1
        self.restaurant_id = Zomato.restaurant_number

        # Add restaurant name to the set
        Zomato.restaurant_names.add(restaurant_name)


# Creating objects
r1 = Zomato("Paradise", {"Biryani": 250, "Chicken 65": 180})

r2 = Zomato("Mehfil", {"Biryani": 220, "Kebab": 200})

r3 = Zomato("Ulavacharu", {"Biryani": 300, "Paneer": 180})


# Displaying instance attributes
print(r1.restaurant_name)
print(r1.items)
print(r1.restaurant_id)

print(r2.restaurant_name)
print(r2.items)
print(r2.restaurant_id)

print(r3.restaurant_name)
print(r3.items)
print(r3.restaurant_id)


print(Zomato.discount)
print(Zomato.coupon)
print(Zomato.restaurant_names)
print(Zomato.restaurant_number)