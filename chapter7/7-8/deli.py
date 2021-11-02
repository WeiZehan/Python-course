sandwich_orders = ['Ham', 'lemon', 'onion']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your "+sandwich+" sandwich")
    finished_sandwiches.append(sandwich)
print("Your sandwich is ready")
for sandwich in finished_sandwiches:
    print(sandwich)
    