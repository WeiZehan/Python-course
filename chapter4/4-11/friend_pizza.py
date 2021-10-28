pizzas = ['cheese', 'fruit', 'durian']
friend_pizza = pizzas[:]
pizzas.append('chocolate')
friend_pizza.append('apple')
for pizza in pizzas:
    print("My favorite pizzas are: " + pizza)
for pizza in friend_pizza:
    print("My friend's favorite pizzas are: "+pizza)