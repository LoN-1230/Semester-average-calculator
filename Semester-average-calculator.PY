print("Hello world")
import sys
cGrade = float(input('Chinese exam grade:\n'))
eGrade = float(input('English exam grade:\n'))
mGrade = float(input('Math exam grade:\n'))
g = (cGrade + eGrade + mGrade)/3

print(g)
#\n = 換行
#float() = 換成浮點數

def printOutStatus(g):
 if g>100 or g<0:
  print('unreasonable grade')
 elif g>70:
  print('You pass the exam')
 elif g<70:
  print('You fail the exam')
 else: 
     print("Your grade is" + str(g))
printOutStatus(cGrade)
printOutStatus(eGrade)
printOutStatus(mGrade)

