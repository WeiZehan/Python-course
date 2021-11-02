pizza = "Please enter pizza ingredients ："
pizza += "(enter 'quit' when you are finished)\n"

while True:
    pizzas = input(pizza)
    if pizzas == 'quit':
        break
    else:
        print("We will add "+pizzas+" to the pizza")
