def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile_01 = build_profile('wei', 'zehan',
                                location='china',
                                field='computer')
user_profile_02 = build_profile('wang', 'doudou',
                                location='china',
                                field='eat')
print(user_profile_01)
print(user_profile_02)
