user = []
if not user:
    print("We need to find some users!")
for greet in user:
    if greet == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + greet + ", thank you for logging in again.")
