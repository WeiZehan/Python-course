active = True
while active:
    age = input("Please enter your age(enter 'quit' when you are finished)\n")
    if age == 'quit':
        active = False
    else:
        num = int(age)
        if num < 3:
            print("Free")
        elif 3 <= num < 12:
            print("10 dollars")
        elif num >= 12:
            print("15 dollars")
