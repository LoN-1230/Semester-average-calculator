import sys
x = float(input("請輸入國文成績"))
y = float(input("請輸入數學成績"))
z = float(input("請輸入英文成績"))
grade = (x + y + z) / 3
if x < 1 or x > 100:
    print("國文成績錯誤")
    sys.exit("成績應在1~100間")
if y < 1 or y > 100:
    print("數學成績錯誤")
    sys.exit("成績應在1~100間")
if z < 1 or z > 100:
    print("英文成績錯誤")
    sys.exit("成績應在1~100間")
else:
  print("學期成績平均是" + str(grade))    
if grade < 70:
    print("小於全班平均")
elif grade == 70:
    print("等於全班平均")
else:
    print("高於全班平均")