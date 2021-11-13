class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name + self.last_name)

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)


user_01 = User('wang', 'doudou')
user_02 = User('wang', 'gouyu')
user_03 = User('wang', 'jue')

user_01.describe_user()
user_02.describe_user()
user_03.describe_user()

user_01.greet_user()
user_02.greet_user()
user_03.greet_user()
