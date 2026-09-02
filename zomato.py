class zomato:
    discount=10
    coupon="ZOMATO50"
    restaurent_names=set()
    restaurent_number=0
    def __init__(self, restaurent_name,items):
        self.restaurent_name=restaurent_name
        self.items=items
        zomato.restaurent_number+=1
        self.restaurent_names.add(restaurent_name)
        self.restaurent_id=zomato.restaurent_number
r1=zomato("paradise",{"Briyani":250,"coke":20})
r2=zomato("Mehfil",{"Briyani":220,"friedrice":125})
print(r1.restaurent_names)
print(r1.items)
print(r1.restaurent_id)
print(r2.restaurent_names)
print(r2.items)
print(r2.restaurent_id)
print(zomato.discount)
print(zomato.coupon)
print(zomato.restaurent_names)
print(zomato.restaurent_number)


class order:
    def __init__(selfself,restaurent):
        self.restaurent=restaurent
    def place_order(selfself, item):
        