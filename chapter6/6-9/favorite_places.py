favorite_place = {
    'weizehan': ['tokyo', 'chengdu'],
    'wanggouyu': ['shanghai','beijing'],
    'wangdoudou': ['swiss','london'],
}
for name, places in favorite_place.items():
    print(name.title()+" favorite places are : ")
    for place in places:
        print("\t"+place.title())
