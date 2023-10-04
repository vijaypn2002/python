import master
Choice=0
print('''1.addition
      2.subtraction
      3.division
      4.multiplication ''')
choice=int(input("select the numbers"))
if choice==1:
    a=int(input('enter a num'))
    b=int(input('enter a num'))
    master.addition(a,b)
if choice==2:
    a=int(input('enter a num'))
    b=int(input('enter a num'))
    master.subtraction(a,b)
if choice==3:
    a=int(input('enter a num'))
    b=int(input('enter a num'))
    master.division(a,b)
if choice==4:
    a=int(input('enter a num'))
    b=int(input('enter a num'))
    master.multiplication(a,b)