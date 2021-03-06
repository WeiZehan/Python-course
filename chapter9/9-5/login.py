class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name + self.last_name)

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_01 = User('wang', 'doudou')
user_01.increment_login_attempts()
print(user_01.login_attempts)
user_01.increment_login_attempts()
print(user_01.login_attempts)
user_01.increment_login_attempts()
print(user_01.login_attempts)
user_01.increment_login_attempts()
print(user_01.login_attempts)
user_01.reset_login_attempts()
print(user_01.login_attempts)