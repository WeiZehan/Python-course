num = {
    'wangdoudou': [23,41],
    'wanggouyu': [12,42],
    'wangjue': [13,65],
    'wangmeili': [45,12],
    'wangkele': [98,57],
    }
for name,nums in num.items():
    print(name.title()+" favorite number are : ")
    for number in nums:
        print("\t"+str(number))
        