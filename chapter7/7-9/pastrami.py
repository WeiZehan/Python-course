sandwich_orders = ['Ham', 'pastrami', 'lemon', 'pastrami', 'onion', 'pastrami']
finished_sandwiches = []
print("The five cigarette pastrami at the deli is sold out")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)
print("Your sandwich is ready")
for sandwich in finished_sandwiches:
    print(sandwich)
