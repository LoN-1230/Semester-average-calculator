import sys
school = input("請輸入學校")
name = input("請輸入名字")
x = float(input("請輸入國文成績"))
y = float(input("請輸入數學成績"))
z = float(input("請輸入英文成績"))
grade = (x + y + z)
average = grade / 3
if x < 1 or x > 100:
    print("上列成績輸入錯誤")
    sys.exit("成績應在1~100間")
if y < 1 or y > 100:
    print("上列有成績輸入錯誤")
    sys.exit("成績應在1~100間")
if z < 1 or z > 100:
    print("上列有成績輸入錯誤")
    sys.exit("成績應在1~100間")
else:
    print("就讀%4s 姓名%3s 總分: %3.2f 學期成績平均是: %3.2f" %(school, name, grade, average))    
if average < 70:
    print("小於全班平均")
elif average == 70:
    print("等於全班平均")

else:
    print("高於全班平均")