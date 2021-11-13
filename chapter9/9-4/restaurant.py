class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name)
        print("The cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print("The "+self.restaurant_name+" is opening ! ")

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,number_served):
        self.number_served += number_served


wdd = Restaurant('wangdoudou','noodles')
wdd.set_number_served(1000)
print(wdd.number_served)
wdd.increment_number_served(300)
print(wdd.number_served)

