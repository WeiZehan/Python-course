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


magicians = ['wanggouyu', 'wangjue', 'laomuzhu']
make_great(magicians)
show_magicians(magicians)
