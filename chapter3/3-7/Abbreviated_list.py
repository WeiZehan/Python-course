dinner=['wangdoudou','weizehan','zhouzhiqi']
print("I invited "+dinner[0]+" to dinner")
print("I invited "+dinner[1]+" to dinner")
print("I invited "+dinner[2]+" to dinner")
#3-4
print(dinner[1]+" can't keep the appointment")
dinner[1]='zhangchaocheng'
print("I invited "+dinner[0]+" to dinner")
print("I invited "+dinner[1]+" to dinner")
print("I invited "+dinner[2]+" to dinner")
#3-5
print("I found a bigger dining table")
dinner.insert(0,'wanggouyu')
dinner.insert(2,'wangjue')
dinner.append('wangyu')
print("I invited "+dinner[0]+" to dinner")
print("I invited "+dinner[1]+" to dinner")
print("I invited "+dinner[2]+" to dinner")
print("I invited "+dinner[3]+" to dinner")
print("I invited "+dinner[4]+" to dinner")
#3-5
print("My newly purchased table cannot be delivered in time, I can only invite two guests")
print("Sorry i can't invite "+dinner.pop(0)+" to dinner")
print("Sorry i can't invite "+dinner.pop(0)+" to dinner")
print("Sorry i can't invite "+dinner.pop(0)+" to dinner")
print("Sorry i can't invite "+dinner.pop(0)+" to dinner")
print("I invited "+dinner[0]+" to dinner")
print("I invited "+dinner[1]+" to dinner")
del dinner[0]
del dinner[0]
print(dinner)