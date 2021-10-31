favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

not_survey = ['wanggouyu', 'wangdoudou']
for person in not_survey:
    if person not in favorite_languages.keys():
        print(person.title()+" , please take survey.")

for people in favorite_languages.keys():
    print("Thanks for you survey , "+str(people.title()))
