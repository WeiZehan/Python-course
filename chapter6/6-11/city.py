cities = {
    'chengdu': {
        'country': 'China',
        'food': 'huoguo',
    },
    'beijing': {
        'country': 'China',
        'food': 'kaoya',
    },
    'shanghai': {
        'country': 'China',
        'food': 'shengjian',
    },
}
for city_name, city_info in cities.items():
    print("City name is "+city_name+" : ")
    print('country : '+city_info['country'])
    print('food : '+city_info['food'])
