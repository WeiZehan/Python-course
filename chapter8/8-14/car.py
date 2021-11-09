def make_car(brand, model, **car_info):
    car = {}
    car['brand'] = brand
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car


car_01 = make_car('subaru', 'outback', color='blue', tow_package=True)
car_02 = make_car('dazhong', 'outback', color='black', tow_package=False)
print(car_01)
print(car_02)
