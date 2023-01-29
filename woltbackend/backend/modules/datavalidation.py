from datetime import datetime

# class and method will check if REQUEST data in POST request is in correct format and values are logical
# raises a ValueError if data seems illogical (for example cart value -1€)
# raises a KeyError if dictionary value is not in wanted format

class DataValidator:
    def __init__(self, obj: dict):
        self.obj = obj

    def validate_data(self):
        try:
            cart_value = self.obj['cart_value']
            if type(cart_value) != int or cart_value < 0:
                raise ValueError
        except KeyError:
            pass
        try:
            delivery_distance = self.obj['delivery_distance']
            if type(delivery_distance) != int or delivery_distance < 0:
                raise ValueError
        except KeyError:
            pass
        try:
            number_of_items = self.obj['number_of_items']
            if type(number_of_items) != int or number_of_items < 1:
                raise ValueError
        except KeyError:
            pass
        try:
            time = self.obj['time']
            if type(time) != str:
                raise ValueError
            try:
                ISOtime = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
            except ValueError:
                pass
        except KeyError:
            pass

        return self