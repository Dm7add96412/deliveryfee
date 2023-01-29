from datetime import datetime

# calculations for delivery fee

class DataCalculator:
    def __init__(self, obj: dict):
        self.cart_value = obj['cart_value']
        self.delivery_distance = obj['delivery_distance']
        self.number_of_items = obj['number_of_items']
        self.timeISO = obj['time']

# check if cart value is less than 10€ and return reduction if true
    def calc_cartfee(self):
        if self.cart_value < 1000:
            return 1000 - self.cart_value
        else:
            return 0

# check if distance is more than 1km. for each next 500m an additional 1€ subcharge is added
    def calc_distance(self):
        i = 1000
        fee = 200
        if self.delivery_distance <= i:
            return fee
        while i <  self.delivery_distance:
            i += 500
            fee += 100
        return fee

# check if number of items is more than 5 when additional 0,5€ subcharge is added to each item
# if number of items is more than 12 an additional 1,2€ fee is added
    def calc_items(self):
        i = 5
        fee = 0
        if self.number_of_items < i:
            return 0
        if self.number_of_items > 12:
            fee = 120
        while i < self.number_of_items:
            i += 1
            fee += 50
        fee += 50
        return fee

# check if order has been made on Friday 3PM - 7PM, when total order is multiplied by 1,2
    def check_time(self):
        timeobject = datetime.strptime(self.timeISO, "%Y-%m-%dT%H:%M:%SZ")
        weekday = timeobject.isoweekday()
        min_time = datetime(2023, 1, 1, 15)
        max_time = datetime(2023, 1, 1, 19)
        if weekday != 5:
            return 1
        if timeobject.time() >= min_time.time() and timeobject.time() <= max_time.time():
            return 1.2
        return 1