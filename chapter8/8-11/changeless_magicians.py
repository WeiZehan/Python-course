def show_magicians(names):
    for name in names:
        print(name)


def make_great(names):
    great_magicians = []
    while names:
        magician = names.pop()
        great_magician = " the Great " + magician.title()
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        names.append(great_magician)

    return names


magicians = ['wanggouyu', 'wangjue', 'laomuzhu']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians)
