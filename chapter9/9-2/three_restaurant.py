class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name)
        print("The cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print("The "+self.restaurant_name+" is opening ! ")


restaurant_01 = Restaurant('wangdoudou','piantang')
restaurant_02 = Restaurant('wanggouyu','zhaji')
restaurant_03 = Restaurant('wangjue','hanbaowang')

restaurant_01.describe_restaurant()
restaurant_02.describe_restaurant()
restaurant_03.describe_restaurant()
