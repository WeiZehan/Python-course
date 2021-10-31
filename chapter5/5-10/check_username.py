current_users = ['wangjue', 'wangdoudou', 'wanggouyu', 'laomuzhu', 'wangzhuyu']
new_users = ['Wangjue', 'Wanggouyu', 'wangmeili', 'wangkele', 'wangyu']
for user in new_users:
    if user.lower() in current_users:
        print(user+" ，please enter another username.")
    else:
        print(user+" ,this username is not used.")

