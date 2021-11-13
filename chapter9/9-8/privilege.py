"""
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name + self.last_name)

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print("- " + privilege)

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges =privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


admin = Admin('wang','doudou')

admin.describe_user()

admin.privileges.

print("\nAdding privileges...")
admin_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
admin.privileges.privileges = admin_privileges
admin.privileges.show_privileges()
"""