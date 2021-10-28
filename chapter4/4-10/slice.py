animals = ['dog', 'cat', 'wangdoudou', 'wanggouyu']
for animal in animals:
    print(animal + " would make a great pet")
print("any of these animals would make a great pet")
# 4-2
for animal in animals[:3]:
    print("The first three animals in the list are: "+animal)
for animal in animals[1:4]:
    print("Three items from the middle of the list are: "+animal)
for animal in animals[-3:]:
    print("The last three items in the list are: "+animal)
