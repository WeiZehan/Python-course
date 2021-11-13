class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name)
        print("The cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print("The " + self.restaurant_name + " is opening ! ")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'milk']

    def show_icecream(self):
        for flavor in self.flavors:
            print(flavor)


icecream = IceCreamStand('wangdoudou','ice')
icecream.show_icecream()
