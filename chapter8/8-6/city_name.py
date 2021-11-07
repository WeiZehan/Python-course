def city_country(name, country):
    information = '"' + name.title() + ", " + country.title() + '"'
    return information


while True:
    name = input("Please enter your name: ")
    country = input("Please enter your country: ")
    if name == 'q' or country == 'q':
        break
    full = city_country(name, country)
    print(full)
