active = True
place = "If you could visit one place in the world, where would you go?"
place += "\n(enter 'quit' when you are finished)\n"
places = []
while active:
    temp = input(place)
    if temp == 'quit':
        active = False
    else:
        places.append(temp)
print("Dream resort : ")
for place in places:
    print(place)
